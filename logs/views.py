from main.models import Log, Group
from main.utils import userAuthentication, responseJsonUtil, getPropertyByName, getUserByRequest
from logs.serializers import LogSerializer
from logs.deserializers import logDeserializer
from django.http import HttpResponse
from django.db import transaction
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
        tmpResultLogs = Log.objects.raw('select * from main_log where user_id = '+str(getUserByRequest(request).id)+' and group_id = ' + group+' and date ="'+tmpDate+'"')
        tmpSerializer = LogSerializer(tmpResultLogs)
        return responseJsonUtil(True, None, tmpSerializer)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        tmpActivities = getPropertyByName('activities', data.items())
        with transaction.commit_on_success():
            deleteLog(getUserByRequest(request).id, getPropertyByName('group', data.items()), getPropertyByName('date', data.items()))
            for tmpObject in tmpActivities:
                tmpLog = logDeserializer(tmpObject)
                tmpLog.save()
            return responseJsonUtil(True, None, None)
        return responseJsonUtil(False, None, None)


def deleteLog(argUser, argGroup, argDate):
    Log.objects.filter(user=argUser, group=Group.objects.get(pk=argGroup), date=argDate).update(entity_status=1)
