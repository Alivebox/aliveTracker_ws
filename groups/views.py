from main.models import Group, Project
from main.utils import *
from groups.serializers import GroupSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from datetime import date
from django.db import connection
from projects.dtos import UserDTO
from projects.serializers import userListSerializer
from django.db import connection, transaction


@api_view(['DELETE', 'POST', 'PUT'])
def groupsServices(argRequest, format=None):
    if userAuthentication(argRequest):
        if argRequest.method == 'POST':
            try:
                tmpData = JSONParser().parse(argRequest)
                tmpNewGroup = Group.objects.create(name=getPropertyByName('name', tmpData.items()),
                                                   description=getPropertyByName('description', tmpData.items()),
                                                   logo_url=getPropertyByName('logo_url', tmpData.items()),
                                                   web_site_url=getPropertyByName('web_site_url', tmpData.items()),
                                                   created=date.today())

                tmpUser = getUserByRequest(argRequest)
                Group_User.objects.create(user=tmpUser,
                                          group=tmpNewGroup,
                                          role=getAdminRole())
                tmpSerializer = GroupSerializer(tmpNewGroup)
                return responseJsonUtil(True, None, tmpSerializer)
            except BaseException:
                return responseJsonUtil(False, 'ERROR000', None)
        if argRequest.method == 'PUT':
            try:
                tmpData = JSONParser().parse(argRequest)
                Group.objects.filter(id=getPropertyByName('id', tmpData.items())).update(
                    name=getPropertyByName('name', tmpData.items()),
                    description=getPropertyByName('description', tmpData.items()),
                    logo_url=getPropertyByName('logo_url', tmpData.items()),
                    web_site_url=getPropertyByName('web_site_url', tmpData.items()))
                modifiedGroup = Group.objects.get(id=getPropertyByName('id', tmpData.items()))
                tmpSerializer = GroupSerializer(modifiedGroup)
                return responseJsonUtil(True, None, tmpSerializer)
            except Group.DoesNotExist:
                return responseJsonUtil(False, 'ERROR000', None)
    else:
        return responseJsonUtil(False, 'ERROR103', None)


@api_view(['GET'])
def getGroupsByUser(request, format=None):
    if userAuthentication(request):
        if request.method == 'GET':
            try:
                tmpUser = getUserByRequest(request)
                tmpMyGroups = Group.objects.raw(
                    'select * from main_group where id in ( select group_id from main_group_user where user_id=' + str(
                        tmpUser.pk) + ' and role_id =1 ) and entity_status = 0')
                tmpBelongToGroups = Group.objects.raw(
                    'select * from main_group where id in ( select group_id from main_group_user where user_id=' + str(
                        tmpUser.pk) + ' and role_id <>1 ) and entity_status = 0')
                tmpMyGroupsSerializer = GroupSerializer(tmpMyGroups)
                tmpBelongToGroupsSerializer = GroupSerializer(tmpBelongToGroups)
                data = {'myGroups': tmpMyGroupsSerializer.data, 'belongToGroups': tmpBelongToGroupsSerializer.data}
                return rawResponseJsonUtil(True, None, data)
            except User.DoesNotExist:
                return responseJsonUtil(False, 'ERROR400', None)
    else:
        return responseJsonUtil(False, 'ERROR103', None)

@api_view(['DELETE'])
def deleteGroupProcess(argRequest, argGroupID):
    if userIsGroupAdmin(argRequest, argGroupID):
        try:
            Group.objects.filter(id=argGroupID).update(entity_status=1)
            Project.objects.filter(group=argGroupID).update(entity_status=1)
            return responseJsonUtil(True, None, None)
        except BaseException:
            return responseJsonUtil(False, 'ERROR000', None)
    else:
        return responseJsonUtil(False, 'ERROR103', None)

    return responseJsonUtil(True, None, None)


@api_view(['GET'])
def getUsersByGroup(argRequest, argGroupID, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR103', None)

    if argRequest.method == 'GET':
        try:
            cursor = connection.cursor()
            cursor.execute('select muser.id as id, muser.email as name, mrole.name as role \
            from main_group_user group_user inner join main_user muser on muser.id = group_user.user_id \
            inner join main_role mrole on group_user.role_id = mrole.id \
            where muser.entity_status = 0 and group_user.group_id = ' + str(argGroupID))
            tmpResult = cursor.fetchall()
            connection.close()
            tmpUserSerializer = convertUserRole(tmpResult)
            return rawResponseJsonUtil(True, None, tmpUserSerializer)
        except BaseException:
            return responseJsonUtil(False, 'ERROR309', None)


# Get the query result to serialize
def convertUserRole(argUserRoleResult):
    tmpList = []
    for tmpItem in argUserRoleResult:
        tmpUserDTO = UserDTO(id=tmpItem[0],
                             name=tmpItem[1],
                             role=tmpItem[2])
        tmpUserDTOSerializer = userListSerializer(tmpUserDTO)
        tmpList.append(tmpUserDTOSerializer.data)
    return tmpList


@api_view(['POST', 'PUT'])
def updateUserRole(argRequest, format=None):
    if not userAuthentication(argRequest):
        return responseJsonUtil(False, 'ERROR103', None)

    try:
        tmpData = JSONParser().parse(argRequest)
        tmpGroupId = getPropertyByName('id', tmpData.items())
        deleteUsersBelongGroup(tmpGroupId)
        insertProjectUsers(tmpData, tmpGroupId)
        return responseJsonUtil(True, None, None)
    except Group_User.DoesNotExist:
        return responseJsonUtil(False, 'ERROR300', None)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)



# Delete all users that belong to a project
def deleteUsersBelongGroup(argGroupId):
    cursor = connection.cursor()
    cursor.execute('delete from main_group_user where group_id = ' + str(argGroupId))
    transaction.commit_unless_managed()
    connection.close()



# Insert project_user
def insertProjectUsers(argGroupUsers, argGroupID):
    tmpList = getPropertyByName('users', argGroupUsers.items())
    for tmpCont in range(len(tmpList)):
        Group_User.objects.create(user=User.objects.get(pk=getPropertyByName('id', tmpList[tmpCont].items())),
                                    group=Group.objects.get(pk=argGroupID),
                                    role=Role.objects.get(name=getPropertyByName('role', tmpList[tmpCont].items())))
