from main.models import User
from main.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pdb;


class UserAuthentication(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, email):
        try:
            pdb.set_trace();
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        pdb.set_trace();
        user = self.get_object(email)
        serializer = UserSerializer(user)
        return Response(serializer.data)