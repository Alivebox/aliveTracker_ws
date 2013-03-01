from main.models import User, Group_User, Project_User, User_Forgot_Password
from main.serializers import UserSerializer, PermissionGroupDTOSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, getPropertyByName, sendEmail, tokenGenerator, md5Encoding, emailExists, correctForgotPasswordToken
from rest_framework.parsers import JSONParser

@api_view(['GET','POST'])
def user_authentication(request, format=None):

    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        user = User.objects.get(password=tmpPassword,email=tmpMail,entity_status=0)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return responseJsonUtil(True, None, serializer)



@api_view(['GET'])
def user_permissions(request, format=None):

    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        user = User.objects.get(password=tmpPassword,email=tmpMail,entity_status=0)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = getGroupPermissionsByUser(user)
    return responseJsonUtil(True, None, serializer)



def getGroupPermissionsByUser(user):
    tmpResultGroups = Group_User.objects.raw('Select * from main_group_user usergroup inner join (\
            Select permission.id as idPermission, permission.name as namePermission, role.id  as idRole, role.name as roleName from main_permission_roles permroles inner join  main_permission permission on permission.id = permroles.permission_id, main_role role \
            where permission.entity_status = 0 \
            and  role.id = permroles.role_id \
            and role.entity_status = 0) \
            rolePermissions on usergroup.role_id = rolePermissions.idRole \
        where usergroup.user_id = ' + str(user.pk))
    serializer = PermissionGroupDTOSerializer(tmpResultGroups)
    return serializer



def getProjectPermissionsByUser(user):
    tmpResultProjects = Project_User.objects.raw('Select * from main_project_user userproject inner join (\
            Select permission.id as idPermission, permission.name as namePermission, role.id  as idRole, role.name as roleName from main_permission_roles permroles inner join  main_permission permission on permission.id = permroles.permission_id, main_role role \
            where permission.entity_status = 0 \
            and  role.id = permroles.role_id \
            and role.entity_status = 0) rolePermissions on userproject.role_id = rolePermissions.idRole \
        where userproject.user_id = ' + str(user.pk))
    serializer = PermissionGroupDTOSerializer(tmpResultProjects)
    return serializer



@api_view(['POST'])
def register_user(request, format=None):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        tmpUserSerializer = UserSerializer(data=data)
        if tmpUserSerializer.is_valid():
            tmpUserSerializer.save()
            return responseJsonUtil(True, None, tmpUserSerializer)
        else:
            return responseJsonUtil(False, 'ERROR01',  None)


@api_view(['PUT'])
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




