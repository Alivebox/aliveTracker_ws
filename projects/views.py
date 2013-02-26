from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from main.models import Project
from projects.serializers import ProjectSerializer


@api_view(['GET'])
def retrieveAllProjectsByGroup(request, format=None):
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return HttpResponse(json.dumps({'success': True, 'error': None, 'result': serializer.data}),
                            content_type='application/json')
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


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
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteProject(request, format=None):
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateProjectsUserList(request, format=None):
    try:
        tmpProject = Project.objects.all()
        serializer = ProjectSerializer(tmpProject)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
