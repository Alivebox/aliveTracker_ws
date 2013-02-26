from main.models import Group_User
from main.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
#import rpdb2


@api_view(['GET','POST'])
def retrieveMyGroups(request, argPassword, argUserID, argUserName, format=None):

    #rpdb2.start_embedded_debugger('xyz')
    try:
        tmpGroup = Group_User.objects.get(password=argPassword,user=argUserName,entity_status=0)
    except Group_User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(tmpGroup)
        return Response(serializer.data)


@api_view(['GET','POST'])
def retrieveGroupsIBelongTo(request, argPassword, argUserID, argUserName, format=None):

    try:
        tmpGroup = Group_User.objects.get(password=argPassword,user=argUserName,entity_status=0)
    except Group_User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(tmpGroup)
        return Response(serializer.data)