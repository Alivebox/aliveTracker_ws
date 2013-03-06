from main.models import Log, Group, Project, User
from logs.logReports import *
from main.utils import *
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


@api_view(['POST','GET'])
def exportReport(request, format=None):
    if request.method == 'GET':
        reportBook = buildReport(3, 0, 0,0,'2012-01-01','2013-03-01')
        return buildExcelFileResponse('logReport.xls', reportBook)
    if userAuthentication(request):
        if request.method == 'POST':
            data = JSONParser().parse(request)
            tmpGroupID = getPropertyByName('groupId',data.items())
            tmpProjectID = getPropertyByName('projectId',data.items())
            tmpUserID = getPropertyByName('userId',data.items())
            tmpDateRangeId = getPropertyByName('dateRangeId',data.items())
            tmpStartDate = getPropertyByName('startDate',data.items())
            tmpEndDate = getPropertyByName('endDate',data.items())
            errorCode = exportReportPermissionsValidation(tmpGroupID, tmpProjectID, tmpUserID)
            if errorCode != None:
                return responseJsonUtil(False, errorCode,  None)
            reportBook = buildReport(tmpGroupID, tmpProjectID, tmpUserID,tmpDateRangeId,tmpStartDate,tmpEndDate)
            return buildExcelFileResponse('logReport.xls', reportBook)
    else:
        return responseJsonUtil(False, 'ERROR100',  None)


def exportReportPermissionsValidation(argGroupID,argProjectID,argUserID):
    try:
        Group.objects.get(id = argGroupID)
    except:
        return 'ERROR200'
    if argProjectID!=0:
        try:
            Project.objects.get(id = argProjectID)
        except:
            return 'ERROR500'
    if argUserID!=0:
        try:
            User.objects.get(id = argUserID)
        except:
            return 'ERROR400'
    return None


