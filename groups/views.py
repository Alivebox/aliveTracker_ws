from main.models import Group_User, Group
from main.utils import responseJsonUtil, userAuthentication, getPropertyByName
from groups.serializers import GroupSerializer, LogSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET','PUT','POST'])
def myGroupsServices(request, format=None):

    if request.method == 'GET':
        tmpUserID= request.META['HTTP_USER_ID']
        tmpResult = Group.objects.raw('select * from main_group where id in ( select group_id from main_group_user where user_id='+str(tmpUserID)+' and role_id =1)')
        serializer = GroupSerializer(tmpResult)
        return Response(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        newGroup = Group.objects.create(name=getPropertyByName('name',data.items()), description=getPropertyByName('description',data.items()),  logo_url=getPropertyByName('logo_url',data.items()),  web_site_url=getPropertyByName('web_site_url',data.items()),  created='2013-01-31')
        return responseJsonUtil(True, None, newGroup)


@api_view(['GET'])
def retrieveGroupsIBelongTo(request, format=None):

    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        tmpUserID= request.META['HTTP_USER_ID']
        tmpResult = Group.objects.raw('select * from main_group where id in ( select group_id from main_group_user where user_id='+str(tmpUserID)+' and role_id <> 1)')

    except Group_User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(tmpResult)
        return Response(serializer.data)


@api_view(['POST'])
def addLogEntry(request, format=None):

    if not userAuthentication(request):
        Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'POST':
        # add code
        data = JSONParser().parse(request)
        tmpLogSerializer = LogSerializer(data=data)
        if tmpLogSerializer.is_valid():
            tmpLogSerializer.save()
            return JSONResponse(tmpLogSerializer.data, status=201)
        else:
            return JSONResponse(tmpLogSerializer.errors, status=400)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)