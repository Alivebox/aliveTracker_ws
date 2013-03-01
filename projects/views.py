from main.models import Project, Project_User, Group
from projects.serializers import ProjectSerializer, ProjectUserDTOSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, userAuthentication, getPropertyByName
from rest_framework.parsers import JSONParser
from projects.deserializers import projectDeserializer


# Returns users who belongs to the respective ID
@api_view(['GET'])
def retrieveUsersByProject(argRequest, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_10', None)

    tmpProjectID = argRequest.META['HTTP_PROJECT_ID']
    tmpResult = Project_User.objects.raw('select project_user.id, project_user.project_id, project_user.user_id, project_user.role_id, muser.name as userName, mrole.name as roleName\
    from main_project_user project_user inner join main_user muser on project_user.user_id = muser.id inner join main_role mrole on project_user.role_id = mrole.id \
    where project_user.project_id =  ' + str(tmpProjectID))
    serializer = ProjectUserDTOSerializer(tmpResult)
    return responseJsonUtil(True, None, serializer)


# Project Services
@api_view(['POST', 'PUT', 'GET'])
def projectServices(argRequest, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_10', None)

    if argRequest.method == 'GET':
        tmpGroupID = argRequest.META['HTTP_GROUP_ID']
        tmpResult = Project.objects.raw('select * from main_project where group_id =  ' + str(tmpGroupID))
        serializer = ProjectSerializer(tmpResult)
        return responseJsonUtil(True, None, serializer)

    if argRequest.method == 'POST':
        tmpData = JSONParser().parse(argRequest)
        tmpProject = projectDeserializer(tmpData)
        tmpProject.save()
        tmpProjectSerializer = ProjectSerializer(tmpProject)
        return responseJsonUtil(True, None, tmpProjectSerializer)

    if argRequest.method == 'PUT':
        tmpData = JSONParser().parse(argRequest)
        Project.objects.filter(id=getPropertyByName('id', tmpData.items())).update(
            name=getPropertyByName('name', tmpData.items()),
            description=getPropertyByName('description', tmpData.items()),
            created=getPropertyByName('created', tmpData.items()),
            group=Group.objects.get(pk=getPropertyByName('group', tmpData.items())))
        tmpProject = Project.objects.get(id=getPropertyByName('id', tmpData.items()))
        tmpSerializer = ProjectSerializer(tmpProject)
        return responseJsonUtil(True, None, tmpSerializer)


@api_view(['DELETE'])
def deleteProject(argRequest, argId, format=None):
    # if not userAuthentication(argRequest):
    #     return responseJsonUtil(False, 'ERROR_10', None)

    if argRequest.method == 'DELETE':
        Project.objects.filter(id=argId).update(entity_status=1)
        tmpProject = Project.objects.filter(id=argId)
        tmpSerializer = ProjectSerializer(tmpProject)
        return responseJsonUtil(True, None, tmpSerializer)


@api_view(['PUT'])
def updateProjectsUserList(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
