from os import tmpnam
from main.models import User, Group_User, Project_User, User_Forgot_Password, Group, Role
from main.serializers import UserSerializer, PermissionGroupDTOSerializer,UserDTOSerializer, UserSerializerDTO, \
    RoleSerializer
from main.utils import userAuthentication, projectExists, groupExists, userIsGroupAdmin
import json
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, getPropertyByName, sendEmail, tokenGenerator, md5Encoding, emailExists, \
    correctForgotPasswordToken
from rest_framework.parsers import JSONParser
from django.contrib.sessions.backends.db import SessionStore


@api_view(['GET','POST','PUT'])
def user_services(request, pk, format=None):

    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR100',  None)
    if request.method == 'GET':
        return user_authentication(request)
    if request.method == 'POST':
        return register_user(request)
    if request.method == 'PUT':
        return update_user(request, pk)


@api_view(['POST'])
def user_authentication(argRequest, format=None):
    try:
        tmpData = JSONParser().parse(argRequest)
        tmpEmail = str(getPropertyByName('email', tmpData.items()))
        tmpPassword = str(getPropertyByName('password', tmpData.items()))
        tmpUser = User.objects.get(password=tmpPassword, email=tmpEmail, entity_status=0)


        if argRequest.method == 'POST':

            if 'id' not in argRequest.session:
                tmpTokken = md5Encoding(tokenGenerator(16))
                argRequest.session['id'] = tmpTokken
                tmpSession = SessionStore()
                tmpSession.save()
                tmpSessionKey = tmpSession.session_key;
                argRequest.session._session_key = tmpSessionKey
                User.objects.filter(pk=tmpUser.id).update(session_key=tmpSessionKey)
            else:
                User.objects.filter(pk=tmpUser.id).update(session_key=argRequest.session._session_key)

            tmpSerializer = UserSerializerDTO(tmpUser)
            return responseJsonUtil(True, None, tmpSerializer)
    except User.DoesNotExist:
        return responseJsonUtil(False, 'ERROR100',  None)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)


@api_view(['GET'])
def getUserAuth(argRequest, format=None):
    try:
        if userAuthentication(argRequest):
            tmpUser = User.objects.raw('Select * from main_user where session_key = \'' + argRequest.session.session_key +
                                       '\'')
            tmpSerializer = UserSerializer(tmpUser)
            return responseJsonUtil(True, None, tmpSerializer)
        return responseJsonUtil(False, 'ERROR100',  None)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)


@api_view(['GET'])
def user_permissions(request, pk, format=None):

    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        tmpGroup = Group.objects.get(pk=pk, entity_status=0)
        tmpUser = User.objects.get(password=tmpPassword,email=tmpMail,entity_status=0)
        serializer = getGroupPermissionsByUser(tmpUser, tmpGroup)
        return responseJsonUtil(True, None, serializer)
    except User.DoesNotExist:
        return responseJsonUtil(False, 'ERROR100',  None)
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
        where userproject.user_id = ' + str(argUser.pk)+
                                                 ' and userproject.project_id = ' + str(argProject.pk)
    )
    serializer = PermissionGroupDTOSerializer(tmpResultProjects)
    return serializer


@api_view(['GET'])
def getUserByGroupAndProject(request, group, project):
    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR100',  None)
    if not groupExists(group):
        return responseJsonUtil(False, 'ERROR200',  None)
    if not projectExists(project):
        return responseJsonUtil(False, 'ERROR500',  None)
    if not userIsGroupAdmin(request, group):
        return responseJsonUtil(False, 'ERROR309',  None)

    if request.method == 'GET':
        tmpResultUser = User.objects.raw('select * from main_user user '
                                         'inner join (select user_id as userId, role_id as role_id from main_project_user where project_id in '
                                         '(select id from main_project  where group_id = '+str(group)+' and id='+str(project)+' )) tmpProjectUser on  user.id = tmpProjectUser.userId')
        tmpSerializer = UserDTOSerializer(tmpResultUser)
        return responseJsonUtil(True, None, tmpSerializer)


def register_user(request):

    data = JSONParser().parse(request)
    tmpUserSerializer = UserSerializer(data=data)
    if tmpUserSerializer.is_valid():
        tmpUserSerializer.save()
        return responseJsonUtil(True, None, tmpUserSerializer)
    else:
        return responseJsonUtil(False, 'ERROR101',  None)


def update_user(request, pk, format=None):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return responseJsonUtil(False, 404, None)
    data = JSONParser().parse(request)
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return responseJsonUtil(True, None, serializer)
    else:
        return responseJsonUtil(False, 'ERROR01',  None)


@api_view(['GET'])
def getUsers(request, format=None):
    try:
        if not userAuthentication(request):
            return responseJsonUtil(False, 'ERROR100',  None)
        tmpQUERY = request.QUERY_PARAMS
        limit = int(tmpQUERY['limit'])
        tmpFilter = tmpQUERY['filter']
        filtersList = buildFilters(tmpFilter)
        filter = filtersList[0]
        tmpValue = filter["value"]
        tmpValue = tmpValue.replace("%", "")
        tmpProperty = filter["property"]
        tmpResultQuery = User.objects.filter(name__icontains=tmpValue)[:limit]
        serializer = UserSerializer(tmpResultQuery)
        return responseJsonUtil(True, None, serializer)
    except Group.DoesNotExist:
        return responseJsonUtil(False, "ERROR200", None)


def buildFilters(argFilterQueryObject):

    tmpFilter = '{ "filters" : ' + argFilterQueryObject + '}'
    data = json.loads(tmpFilter)
    filtersList = data["filters"]
    return filtersList


@api_view(['POST'])
def forgotPassword(request, format=None):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        TO = getPropertyByName('email',data.items())
        if emailExists(TO):
            code = md5Encoding(tokenGenerator())
            SUBJECT = "AliveTracker forgot password instructions. (DO NOT REPLY)"
            FROM = "team@alivebox.com"
            MESSAGE = """
            Hey, we heard you lost your AliveTracker password.
            Use the following link to reset your password:

                     http://www.alivetracker.com:8000/main/resetPassword/"""+TO+"""/"""+code+"""

            Ignore this email if you haven't experienced any password trouble.

            Thanks,
            AliveTracker Team"""
            try:
                tmpUser = User.objects.get(email=TO)
                User_Forgot_Password.objects.get_or_create(user=tmpUser)
                User_Forgot_Password.objects.filter(user=tmpUser).update(token=code)
            except:
                return responseJsonUtil(False, 'ERROR000',  None)
            try:
                sendEmail(FROM, TO, SUBJECT, MESSAGE)
                return responseJsonUtil(True, None,  None)
            except:
                return responseJsonUtil(False, 'ERROR002',  None)
        else:
            return responseJsonUtil(False, 'ERROR102',  None)


@api_view(['GET'])
def resetPassword(request,email, token,  format=None):

    if request.method == 'GET':

        if correctForgotPasswordToken(email, token):
            TO = email
            tmpPassword = tokenGenerator()
            code = md5Encoding(tmpPassword)
            SUBJECT = "AliveTracker reset password message. (DO NOT REPLY)"
            FROM = "team@alivebox.com"
            MESSAGE = """
            You requested to have your password reset, below is your new password.

                      Username:"""+TO+"""
                      New Password: """+tmpPassword+"""

                      To login your new password, please go to
                      http://www.alivetracker.com
            Thanks,
            AliveTracker Team"""
            try:
                User.objects.filter(email=TO).update(password=code, entity_status=2)
            except:
                return responseJsonUtil(False, 'ERROR000',  None)
            try:
                sendEmail(FROM, TO, SUBJECT, MESSAGE)
                return responseJsonUtil(True, None,  None)
            except:
                return responseJsonUtil(False, 'ERROR002',  None)
        else:
            return responseJsonUtil(False, 'ERROR100',  None)


@api_view(['GET'])
def getRoles(argRequest):
    #if not userAuthentication(argRequest):
     #   return responseJsonUtil(False, 'ERROR100',  None)
    try:
        tmpRoles = Role.objects.all()
        tmpRolesSerializer = RoleSerializer(tmpRoles)
        return responseJsonUtil(True, None, tmpRolesSerializer)
    except Role.DoesNotExist:
        return responseJsonUtil(False, 'ERROR600',  None)