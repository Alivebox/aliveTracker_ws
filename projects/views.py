from main.models import Project, Group, Project_User, Role, User
from projects.serializers import ProjectSerializer, ProjectUserListDTOSerializer, userListSerializer
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, userAuthentication, getPropertyByName, getUserByRequest
from rest_framework.parsers import JSONParser
from projects.deserializers import projectDeserializer
from projects.dtos import ProjectUserListDTO, UserDTO
from django.db import connection, transaction

# Returns users who belongs to the respective ID
@api_view(['GET'])
def getProjectsByUserAndGroup(argRequest, argGroupID, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_100', None)
    try:
        tmpMail = getUserByRequest(argRequest).email
        tmpResult = Project.objects.raw('select  mproject.id, mproject.name, mproject.created, mproject.group_id \
        from main_project_user project_user inner join main_user muser on project_user.user_id = muser.id \
        inner join main_project mproject on project_user.project_id = mproject.id \
        where muser.entity_status = 0 and muser.email= \'' + str(tmpMail) + '\' and mproject.group_id = ' + str(argGroupID))
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
        tmpProjectSerializer = ProjectSerializer(tmpProject)
        cursor = connection.cursor()
        cursor.execute('select muser.id as id, muser.email as name, mrole.name as role\
        from main_project_user project_user inner join main_user muser on muser.id = project_user.user_id \
        inner join main_role mrole on project_user.role_id = mrole.id \
        where muser.entity_status = 0 and project_user.project_id = ' + str(argProjectID))
        tmpResult = cursor.fetchall()
        connection.close()
        tmpUserSerializer = convertUserRole(tmpResult)
        tmpProjectUserListSerializer = createProjectListDTOObject(tmpProjectSerializer, tmpUserSerializer, argProjectID)
        return responseJsonUtil(True, None, tmpProjectUserListSerializer)
    except Project.DoesNotExist:
        return responseJsonUtil(False, 'ERROR_500', None)


# Get the query result to serialize
def convertUserRole(argUserRoleResult):
    tmpList = []
    for tmpItem in argUserRoleResult:
        tmpUserDTO = UserDTO(id=tmpItem[0],
                             name=tmpItem[1],
                             role=tmpItem[2],)
        tmpUserDTOSerializer = userListSerializer(tmpUserDTO)
        tmpList.append(tmpUserDTOSerializer.data)
    return tmpList


# Creates a ProjectListDTO, Using the project model and the userList
def createProjectListDTOObject(argProject, argUserList, argProjectID):
    tmpProjectUserListDTO = ProjectUserListDTO(id=argProjectID,
                                               name=getPropertyByName('name', argProject.data.items()),
                                               created=getPropertyByName('created', argProject.data.items()),
                                               description=getPropertyByName('description', argProject.data.items()),
                                               groupID=getPropertyByName('group', argProject.data.items()),
                                               users=argUserList)
    tmpProjectUserListDTOSerializer = ProjectUserListDTOSerializer(tmpProjectUserListDTO)
    return tmpProjectUserListDTOSerializer


# Save and update projects
@api_view(['POST', 'PUT'])
def saveProject(argRequest, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_100', None)

    tmpData = JSONParser().parse(argRequest)
    if argRequest.method == 'POST':
        tmpProject = projectDeserializer(tmpData)
        tmpProject.save()
        updateUserListInProject(tmpData)
        return responseJsonUtil(True, None, None)
    if argRequest.method == 'PUT':
        Project.objects.filter(id=getPropertyByName('id', tmpData.items())).update(
            name=getPropertyByName('name', tmpData.items()),
            description=getPropertyByName('description', tmpData.items()),
            created=getPropertyByName('created', tmpData.items()),
            group=Group.objects.get(pk=getPropertyByName('group', tmpData.items())))
        return responseJsonUtil(True, None, None)


# Update all users that belong to a project
def updateUserListInProject(argData):
    tmpProjectId = getPropertyByName('id', argData.items())
    deleteUsersBelongProject(tmpProjectId)
    insertProjectUsers(argData)


# Delete all users that belong to a project
def deleteUsersBelongProject(argProjectId):
    cursor = connection.cursor()
    cursor.execute('delete from main_project_user where project_id = ' + str(argProjectId))
    transaction.commit_unless_managed()
    connection.close()


# Insert project_user
def insertProjectUsers(argProjectUsers):
    tmpList = getPropertyByName('users', argProjectUsers.items())
    tmpProjectId = getPropertyByName('id', argProjectUsers.items())
    for tmpProjectUser in tmpList:
        Project_User.objects.create(user=User.objects.get(pk=getPropertyByName('id', tmpProjectUser.items())),
                                    project=Project.objects.get(pk=tmpProjectId),
                                    role=Role.objects.get(pk=getPropertyByName('roleId', tmpProjectUser.items())))



# Creates a Project_User Model to be save into the project
@api_view(['DELETE'])
def deleteProject(argRequest, argId, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR_10', None)

    if argRequest.method == 'DELETE':
        Project.objects.filter(id=argId).update(entity_status=1)
        tmpProject = Project.objects.filter(id=argId)
        tmpSerializer = ProjectSerializer(tmpProject)
        return responseJsonUtil(True, None, tmpSerializer)
