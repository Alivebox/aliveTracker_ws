from main.models import Project, Project_User, Group
from projects.serializers import ProjectSerializer, ProjectUserDTOSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, userAuthentication, getPropertyByName
from rest_framework.parsers import JSONParser

# Returns a list of Projects by Group ID
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


# Save a new project to the DB
@api_view(['POST'])
def addNewProjectToGroup(argRequest, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_10', None)

    if argRequest.method == 'POST':
        tmpData = JSONParser().parse(argRequest)
        tmpProject = Project.objects.create(name=getPropertyByName('name', tmpData.items()),
                                            description=getPropertyByName('description', tmpData.items()),
                                            created=getPropertyByName('created', tmpData.items()),
                                            group=Group.objects.get(pk=getPropertyByName('group', tmpData.items())))
        tmpSerializer = ProjectSerializer(tmpProject)
        return responseJsonUtil(True, None, tmpSerializer)


@api_view(['PUT'])
def updateProject(argRequest, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_10', None)

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
