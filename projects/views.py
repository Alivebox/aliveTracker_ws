from main.models import Project
from projects.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, userAuthentication


@api_view(['GET'])
def retrieveAllProjectsByGroup(argRequest, format=None):
    try:
        if not userAuthentication(argRequest):
            return responseJsonUtil(False, 'ERROR_10', None)

        tmpGroupID = argRequest.META['HTTP_GROUP_ID']
        tmpResult = Project.objects.raw('select * from main_project where group_id =  ' + str(tmpGroupID))
        serializer = ProjectSerializer(tmpResult)
        return responseJsonUtil(True, None, serializer)
    except Project.DoesNotExist:
        return responseJsonUtil(False, 'ERROR_10', None)


@api_view(['GET'])
def retrieveUsersByProject(request, format=None):
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addNewProjectToGroup(request, format=None):
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateProject(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteProject(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateProjectsUserList(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
