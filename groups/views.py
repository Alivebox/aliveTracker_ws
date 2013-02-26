from main.models import Group_User, Group
from groups.serializers import Group_UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def retrieveMyGroups(request, format=None):

    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        tmpUserID= request.META['HTTP_USER_ID']
        tmpResult = Group.objects.raw('select * from main_group where id in ( select group_id from main_group_user where user_id='+str(tmpUserID)+' and role_id =1)')

    except Group_User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(tmpResult)
        return Response(serializer.data)


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

