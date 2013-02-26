from main.models import User
from main.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import rpdb2

@api_view(['GET','POST'])
def user_authentication(request, password, email, format=None):

    try:
         user = User.objects.get(password=password,email=email,entity_status=0)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'POST':
        user = request.DATA
        serializer = UserSerializer(user)
        return Response(serializer.data)



@api_view(['GET','POST'])
def header_caption(request, format=None):

    rpdb2.start_embedded_debugger('abc')
    # Header enviado desde cliente = X-MyHeader
    tmpHeader = request.META['HTTP_X_MYHEADER']
    return Response(tmpHeader)