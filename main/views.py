from os import tmpnam
from main.models import User, Group_User, Project_User, User_Forgot_Password, Group, Role
from main.serializers import UserSerializer, PermissionGroupDTOSerializer, UserDTOSerializer, UserSerializerDTO, \
    RoleSerializer
from main.utils import userAuthentication, projectExists, groupExists, userIsGroupAdmin
import json
import locales
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, getPropertyByName, sendEmail, tokenGenerator, md5Encoding, emailExists, \
    correctForgotPasswordToken, getUserByRequest
from rest_framework.parsers import JSONParser
from django.contrib.sessions.backends.db import SessionStore


@api_view(['GET', 'POST', 'PUT'])
def user_services(request, pk, format=None):
    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR103', None)
    if request.method == 'GET':
        return user_authentication(request)
    if request.method == 'POST':
        return register_user(request)
    if request.method == 'PUT':
        return update_user(request, pk)


@api_view(['POST'])
def register_user(request):
    try:
        data = JSONParser().parse(request)
        tmpNewUser = User.objects.create(email=getPropertyByName('email', data.items()),
                                         password=getPropertyByName('password', data.items()));
        newSessionHandler(request, tmpNewUser);
        tmpUserSerializer = UserSerializer(tmpNewUser)
        return responseJsonUtil(True, None, tmpUserSerializer)
    except BaseException:
        return responseJsonUtil(False, 'ERROR101', None)


@api_view(['POST'])
def user_authentication(argRequest, format=None):
    try:
        tmpData = JSONParser().parse(argRequest)
        tmpEmail = str(getPropertyByName('email', tmpData.items()))
        tmpPassword = str(getPropertyByName('password', tmpData.items()))
        tmpUser = User.objects.exclude(entity_status = 1).get(password=tmpPassword, email=tmpEmail)

        if argRequest.method == 'POST':

            if 'id' not in argRequest.session or argRequest.session._session_key == locales.INVALID_SESSION_KEY:
                newSessionHandler(argRequest, tmpUser)
            else:
                User.objects.filter(pk=tmpUser.id).update(session_key=argRequest.session._session_key)

            tmpSerializer = UserSerializerDTO(tmpUser)
            return responseJsonUtil(True, None, tmpSerializer)
    except User.DoesNotExist:
        return responseJsonUtil(False, 'ERROR400', None)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)

def newSessionHandler(argRequest, argUser):
    tmpToken = md5Encoding(tokenGenerator(16))
    argRequest.session['id'] = tmpToken
    tmpSession = SessionStore()
    tmpSession.save()
    tmpSessionKey = tmpSession.session_key;
    argRequest.session._session_key = tmpSessionKey
    User.objects.filter(pk=argUser.id).update(session_key=tmpSessionKey)

@api_view(['POST'])
def logout(argRequest):
    if argRequest.method == 'POST':
        if 'id' in argRequest.session:
            argRequest.session['id'] = locales.INVALID_SESSION_KEY
            argRequest.session._session_key = locales.INVALID_SESSION_KEY
        return responseJsonUtil(True, None, None)

@api_view(['GET'])
def getUserAuth(argRequest, format=None):
    try:
        if userAuthentication(argRequest):
            tmpUser = User.objects.raw(
                'Select * from main_user where session_key = \'' + argRequest.session.session_key +
                '\'')
            tmpSerializer = UserSerializer(tmpUser)
            return responseJsonUtil(True, None, tmpSerializer)
        return responseJsonUtil(False, 'ERROR103', None)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)


@api_view(['GET'])
def user_permissions(request, pk, format=None):
    try:
        tmpGroup = Group.objects.get(pk=pk, entity_status=0)
        tmpUser = getUserByRequest(request)
        serializer = getGroupPermissionsByUser(tmpUser, tmpGroup)
        return responseJsonUtil(True, None, serializer)
    except User.DoesNotExist:
        return responseJsonUtil(False, 'ERROR100', None)
    except Group.DoesNotExist:
        return responseJsonUtil(False, "ERROR200", None)


def getGroupPermissionsByUser(argUser, argGroup):
    tmpResultGroups = Group_User.objects.raw('Select * from main_group_user usergroup inner join (\
            Select permission.id as idPermission, permission.name as namePermission, role.id  as idRole, role.name as roleName from main_permission_roles permroles inner join  main_permission permission on permission.id = permroles.permission_id, main_role role \
            where permission.entity_status = 0 \
            and  role.id = permroles.role_id \
            and role.entity_status = 0) \
            rolePermissions on usergroup.role_id = rolePermissions.idRole \
        where usergroup.user_id = ' + str(argUser.pk) +
                                             ' and usergroup.group_id = ' + str(argGroup.pk)
    )
    serializer = PermissionGroupDTOSerializer(tmpResultGroups)
    return serializer


def getProjectPermissionsByUser(argUser, argProject):
    tmpResultProjects = Project_User.objects.raw('Select * from main_project_user userproject inner join (\
            Select permission.id as idPermission, permission.name as namePermission, role.id  as idRole, role.name as roleName from main_permission_roles permroles inner join  main_permission permission on permission.id = permroles.permission_id, main_role role \
            where permission.entity_status = 0 \
            and  role.id = permroles.role_id \
            and role.entity_status = 0) rolePermissions on userproject.role_id = rolePermissions.idRole \
        where userproject.user_id = ' + str(argUser.pk) +
                                                 ' and userproject.project_id = ' + str(argProject.pk)
    )
    serializer = PermissionGroupDTOSerializer(tmpResultProjects)
    return serializer


@api_view(['GET'])
def getUserByGroupAndProject(request, group, project):
    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR103', None)
    if not groupExists(group):
        return responseJsonUtil(False, 'ERROR200', None)
    if not projectExists(project):
        return responseJsonUtil(False, 'ERROR500', None)

    if request.method == 'GET':
        tmpResultUser = User.objects.raw('select * from main_user tmpUser '
                                         'inner join (select user_id as userId, role_id as role_id from main_project_user where project_id in '
                                         '(select id from main_project  where group_id = ' + str(
            group) + ' and id=' + str(project) + ' )) tmpProjectUser on  tmpUser.id = tmpProjectUser.userId')
        tmpSerializer = UserDTOSerializer(tmpResultUser)
        return responseJsonUtil(True, None, tmpSerializer)


@api_view(['PUT'])
def update_user(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return responseJsonUtil(False, 404, None)
    data = JSONParser().parse(request)
    tmpName = getPropertyByName('name', data.items())
    tmpPassword = getPropertyByName('password', data.items())
    user.name = tmpName
    user.password = tmpPassword
    user.entity_status = 0
    user.save()
    serializer = UserSerializer(user, data=data)
    return responseJsonUtil(True, None, serializer)


@api_view(['PUT'])
def update_default_group(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return responseJsonUtil(False, 404, None)
    data = JSONParser().parse(request)
    tmpDefaultGroup = getPropertyByName('default_group', data.items())
    user.default_group = tmpDefaultGroup
    user.save()
    serializer = UserSerializer(user, data=data)
    return responseJsonUtil(True, None, serializer)



@api_view(['GET', 'POST'])
def getUsers(argRequest, argEmail, format=None):
    try:
        if not userAuthentication(argRequest):
            return responseJsonUtil(False, 'ERROR103', None)
        tmpLimit = 10
        tmpResult = User.objects.filter(email__icontains=argEmail)[:tmpLimit]
        tmpSerializer = UserSerializer(tmpResult)
        return responseJsonUtil(True, None, tmpSerializer)
    except Group.DoesNotExist:
        return responseJsonUtil(False, "ERROR200", None)


def buildFilters(argFilterQueryObject):
    tmpFilter = '{ "filters" : ' + argFilterQueryObject + '}'
    data = json.loads(tmpFilter)
    filtersList = data["filters"]
    return filtersList


@api_view(['PUT'])
def forgotPassword(request, format=None):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        TO = getPropertyByName('email', data.items())
        if emailExists(TO):
            code = md5Encoding(tokenGenerator())
            SUBJECT = "AliveTracker forgot password instructions. (DO NOT REPLY)"
            FROM = "team@alivebox.com"
            MESSAGE = """
            Hey, we heard you lost your AliveTracker password.
            Use the following link to reset your password:

                     http://www.alivetracker.com/#resetPasswordPage?email=""" + TO + """&token=""" + code + """

            Ignore this email if you haven't experienced any password trouble.

            Thanks,
            AliveTracker Team"""
            try:
                tmpUser = User.objects.get(email=TO)
                User_Forgot_Password.objects.get_or_create(user=tmpUser)
                User_Forgot_Password.objects.filter(user=tmpUser).update(token=code)
            except:
                return responseJsonUtil(False, 'ERROR000', None)
            try:
                sendEmail(FROM, TO, SUBJECT, MESSAGE)
                return responseJsonUtil(True, None, None)
            except:
                return responseJsonUtil(False, 'ERROR002', None)
        else:
            return responseJsonUtil(False, 'ERROR102', None)

@api_view(['PUT'])
def setPassword(request, format=None):
    if request.method == 'PUT':
        if not userAuthentication(request):
            return responseJsonUtil(False, 'ERROR103', None)
        data = JSONParser().parse(request)
        tmpPassword = getPropertyByName('password', data.items())
        User.objects.filter(session_key=request.session._session_key).update(password=tmpPassword)
        tmpUser = getUserByRequest(request)
        tmpSerializer = UserSerializer(tmpUser)
        return responseJsonUtil(True, None, tmpSerializer)

@api_view(['PUT'])
def resetPassword(request, format=None):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        tmpEmail = getPropertyByName('email', data.items())
        tmpToken = getPropertyByName('token', data.items())
        tmpPassword = getPropertyByName('password', data.items())
        if correctForgotPasswordToken(tmpEmail, tmpToken):
            User.objects.filter(email=tmpEmail).update(password=tmpPassword)
            tmpUser = User.objects.get(email=tmpEmail)
            newSessionHandler(request, tmpUser);
            tmpSerializer = UserSerializer(tmpUser)
            return responseJsonUtil(True, None, tmpSerializer)
        else:
            return responseJsonUtil(False, 'ERROR104', None)


def passwordSendEmail(request, format=None):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        email = getPropertyByName('email', data.items())
        token = getPropertyByName('token', data.items())

        if correctForgotPasswordToken(email, token):
            TO = email
            tmpPassword = tokenGenerator()
            code = md5Encoding(tmpPassword)
            SUBJECT = "AliveTracker reset password message. (DO NOT REPLY)"
            FROM = "team@alivebox.com"
            MESSAGE = """
            You requested to have your password reset, below is your new password.

                      Username:""" + TO + """
                      New Password: """ + tmpPassword + """

                      To login your new password, please go to
                      http://www.alivetracker.com
            Thanks,
            AliveTracker Team"""
            try:
                User.objects.filter(email=TO).update(password=code, entity_status=2)
            except:
                return responseJsonUtil(False, 'ERROR000', None)
            try:
                sendEmail(FROM, TO, SUBJECT, MESSAGE)
                return responseJsonUtil(True, None, None)
            except:
                return responseJsonUtil(False, 'ERROR002', None)
        else:
            return responseJsonUtil(False, 'ERROR100', None)


@api_view(['GET'])
def getRoles(argRequest):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR100', None)
    try:
        tmpRoles = Role.objects.all()
        tmpRolesSerializer = RoleSerializer(tmpRoles)
        return responseJsonUtil(True, None, tmpRolesSerializer)
    except Role.DoesNotExist:
        return responseJsonUtil(False, 'ERROR600', None)


@api_view(['DELETE'])
def deleteUser(argRequest, argUserID, argGroupID):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR100', None)
    try:
        tmpGroupUser = Group_User.objects.get(user_id=str(argUserID),
                               group_id=str(argGroupID))
        tmpGroupUser.delete()
        return responseJsonUtil(True, None, None)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)

