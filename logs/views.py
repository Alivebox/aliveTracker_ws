from main.utils import userAuthentication
from groups.serializers import LogSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def myLogsServices(request, format=None):

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
