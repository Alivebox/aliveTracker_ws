from main.models import User, Role
from main.serializers import UserSerializer, RoleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from main.utils import responseJsonUtil, userAuthentication


@api_view(['GET','POST'])
def user_authentication(request, format=None):

    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        user = User.objects.get(password=tmpPassword,email=tmpMail,entity_status=0)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return responseJsonUtil(True, None, serializer)


@api_view(['GET'])
def retrieveAllUserRoles(argRequest, format=None):

    try:
        if not userAuthentication(argRequest):
            return responseJsonUtil(False, 'ERROR_10', None)

        tmpRole = Role.objects.all()
        tmpSerializer = RoleSerializer(tmpRole)
        return responseJsonUtil(True, None, tmpSerializer)
    except Role.DoesNotExist:
        return Response(False, None, None)



