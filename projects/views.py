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
def getProjectsByUserAndGroup(argRequest, argGroupID, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_100', None)
    try:
        tmpMail = argRequest.META['HTTP_USERNAME']
        tmpResult = Project.objects.raw('select  mproject.id, mproject.name, mproject.created, mproject.group_id \
        from main_project_user project_user inner join main_user muser on project_user.user_id = muser.id \
        inner join main_project mproject on project_user.project_id = mproject.id \
        where muser.email= "' + str(tmpMail) + '" and mproject.group_id = ' + str(argGroupID))
        serializer = ProjectSerializer(tmpResult)
        return responseJsonUtil(True, None, serializer)
    except BaseException:
        return responseJsonUtil(False, 'ERROR_500', None)


# Returns users who belongs to the respective ID
@api_view(['GET'])
def getProject(argRequest, argProjectID, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_100', None)
    try:
        tmpProject = Project.objects.get(id=argProjectID)
        serializer = ProjectSerializer(tmpProject)
        return responseJsonUtil(True, None, serializer)
    except Project.DoesNotExist:
        return responseJsonUtil(False, 'ERROR_500', None)


# Project Services
@api_view(['POST', 'PUT'])
def saveProject(argRequest, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_100', None)

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

    
