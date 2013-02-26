from main.models import Group_User
from groups.serializers import Group_UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def retrieveMyGroups(request,  format=None):

    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        tmpUserID= request.META['HTTP_USER_ID']
        tmpGroup = Group_User.objects.get_query_set().filter(user=tmpUserID,role =1)
    except Group_User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Group_UserSerializer(tmpGroup)
        return Response(serializer.data)
