from main.models import Group, Project
from main.utils import *
from groups.serializers import GroupSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import datetime


@api_view(['DELETE', 'POST', 'PUT'])
def groupsServices(request, pk, format=None):
    if userAuthentication(request):
        if request.method == 'DELETE':
            if groupExists(pk):
                return deleteGroupProcess(request, pk)
            else:
                return responseJsonUtil(False, 'ERROR200',  None)
        if request.method == 'POST':
            try:
                data = JSONParser().parse(request)
                newGroup = Group.objects.create(name=getPropertyByName('name',data.items()), description=getPropertyByName('description',data.items()),  logo_url=getPropertyByName('logo_url',data.items()),  web_site_url=getPropertyByName('web_site_url',data.items()),  created=datetime.datetime.now())
                serializer = GroupSerializer(newGroup)
                return responseJsonUtil(True, None, serializer)
            except:
                return responseJsonUtil(False, 'ERROR000', None)
        if request.method == 'PUT':
            try:
                data = JSONParser().parse(request)
                Group.objects.filter(id=getPropertyByName('id',data.items())).update(name=getPropertyByName('name',data.items()), description=getPropertyByName('description',data.items()),  logo_url=getPropertyByName('logo_url',data.items()),  web_site_url=getPropertyByName('web_site_url',data.items()))
                modifiedGroup = Group.objects.get(id=getPropertyByName('id',data.items()))
                serializer = GroupSerializer(modifiedGroup)
                return responseJsonUtil(True, None, serializer)
            except:
                return responseJsonUtil(False, 'ERROR000', None)
    else:
        return responseJsonUtil(False, 'ERROR100',  None)



@api_view(['GET'])
def getGroupsByUser(request, format=None):
    if userAuthentication(request):
        if request.method == 'GET':
            try:
                tmpUser = retrieveUser(request)
                tmpMyGroups = Group.objects.raw('select * from main_group where id in ( select group_id from main_group_user where user_id='+str(tmpUser.pk)+' and role_id =1 ) and entity_status = 0')
                tmpBelongToGroups = Group.objects.raw('select * from main_group where id in ( select group_id from main_group_user where user_id='+str(tmpUser.pk)+' and role_id <>1 ) and entity_status = 0')
                tmpMyGroupsSerializer = GroupSerializer(tmpMyGroups)
                tmpBelongToGroupsSerializer = GroupSerializer(tmpBelongToGroups)
                data = {'myGroups':tmpMyGroupsSerializer.data, 'belongToGroups': tmpBelongToGroupsSerializer.data}
                return rawResponseJsonUtil(True, None,data)
            except:
                return responseJsonUtil(False, 'ERROR000',  None)
    else:
        return responseJsonUtil(False, 'ERROR100',  None)



def deleteGroupProcess(argRequest, argGroupID):
    try:
        if userIsGroupAdmin(argRequest,argGroupID):
            try:
                Group.objects.filter(id=argGroupID).update(entity_status=1)
                Project.objects.filter(group=argGroupID).update(entity_status=1)
                return responseJsonUtil(True, None,  None)
            except:
                return responseJsonUtil(False, 'ERROR000',  None)
        else:
            return responseJsonUtil(False, 'ERROR314',  None)
    except:
        return responseJsonUtil(True, None, None)