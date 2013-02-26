from main.models import Group_User
from groups.serializers import Group_UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import rpdb2
import json


@api_view(['GET'])
def retrieveMyGroups(request,  format=None):

    try:
        # tmpMail = request.META['HTTP_USERNAME']
        # tmpPassword = request.META['HTTP_PASSWORD']
        # tmpUserID= request.META['HTTP_USER_ID']
        # tmpGroup = Group_User.objects.get_query_set().filter(user=tmpUserID,role =1)
        tmpGroup_User = Group_User.objects.get_query_set().filter(user=16,role =1)
        rpdb2.start_embedded_debugger('xyz')
        for item in tmpGroup_User:
            print item.group_id

    except Group_User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Group_UserSerializer(tmpGroup_User)
        return Response(serializer.data)
