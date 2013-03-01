from main.models import Group_User, Group, Project
from main.utils import responseJsonUtil, userAuthentication, getPropertyByName
from groups.serializers import GroupSerializer, LogSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET','PUT','POST','DELETE'])
def myGroupsServices(request, format=None):

    if request.method == 'GET':
        try:
            tmpUserID= request.META['HTTP_USER_ID']
            tmpResult = Group.objects.raw('select * from main_group where id in ( select group_id from main_group_user where user_id='+str(tmpUserID)+' and role_id =1 ) and entity_status = 0')
            serializer = GroupSerializer(tmpResult)
            return responseJsonUtil(True, None, serializer)
        except:
            return responseJsonUtil(True, None, None)

    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            newGroup = Group.objects.create(name=getPropertyByName('name',data.items()), description=getPropertyByName('description',data.items()),  logo_url=getPropertyByName('logo_url',data.items()),  web_site_url=getPropertyByName('web_site_url',data.items()),  created='2013-01-31')
            serializer = GroupSerializer(newGroup)
            return responseJsonUtil(True, None, serializer)
        except:
            return responseJsonUtil(True, None, None)

    if request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            Group.objects.filter(id=getPropertyByName('id',data.items())).update(name=getPropertyByName('name',data.items()), description=getPropertyByName('description',data.items()),  logo_url=getPropertyByName('logo_url',data.items()),  web_site_url=getPropertyByName('web_site_url',data.items()),  created='2013-01-31')
            modifiedGroup = Group.objects.get(id=getPropertyByName('id',data.items()))
            serializer = GroupSerializer(modifiedGroup)
            return responseJsonUtil(True, None, serializer)
        except:
            return responseJsonUtil(True, None, None)

    if request.method == 'DELETE':
        try:
            data = JSONParser().parse(request)
            Group.objects.filter(id=getPropertyByName('id',data.items())).update(entity_status=1)
            Project.objects.filter(group=getPropertyByName('id',data.items())).update(entity_status=1)
        except:
            return responseJsonUtil(True, None, None)


@api_view(['GET'])
def groupsIBelongServices(request, format=None):

    if request.method == 'GET':
        try:
            tmpUserID= request.META['HTTP_USER_ID']
            tmpResult = Group.objects.raw('select * from main_group where id in ( select group_id from main_group_user where user_id='+str(tmpUserID)+' and role_id <>1 ) and entity_status = 0')
            serializer = GroupSerializer(tmpResult)
            return responseJsonUtil(True, None, serializer)
        except:
            return responseJsonUtil(True, None, None)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)