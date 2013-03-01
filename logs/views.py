from main.models import Log, Group
from main.utils import userAuthentication, responseJsonUtil, getPropertyByName, stringToDate
from logs.serializers import LogSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST',])
def myLogsServices(request, group, format=None):

    if not userAuthentication(request):
        Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        tmpDate = getPropertyByName("date",request.QUERY_PARAMS.items())
        tmpResultLogs = Log.objects.raw('select * from main_log where group_id = ' + group)
        serializer = LogSerializer(tmpResultLogs)
        return responseJsonUtil(True, None, serializer)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        tmpLogSerializer = LogSerializer(data=data)
        if tmpLogSerializer.is_valid():
            tmpLogSerializer.save()
            return JSONResponse(tmpLogSerializer.data, status=201)
        else:
            return JSONResponse(tmpLogSerializer.errors, status=400)#response json util

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
