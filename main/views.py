from main.models import User, Group_User, Project_User
from main.serializers import UserSerializer, PermissionGroupDTOSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, userAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

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
            return responseJsonUtil(tmpUserSerializer)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)