from main.models import Project
from main.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import rpdb2


@api_view(['GET'])
def retrieveUsersByProject(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = UserSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addNewProjectToGroup(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = UserSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateProject(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = UserSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteProject(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = UserSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateProjectsUserList(request, format=None):
    # rpdb2.start_embedded_debugger('xyz')
    try:
        tmpProject = Project.objects.all()
        serializer = UserSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
