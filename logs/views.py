from main.models import Log, Group
from main.utils import *
from logs.logReports import *
from logs.serializers import LogSerializer
from logs.deserializers import logDeserializer
from django.db import transaction
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['GET','POST',])
def myLogsServices(request, group, format=None):

    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR100',  None)

    if request.method == 'GET':
        if not groupExists(group):
            return responseJsonUtil(False, 'ERROR200',  None)
        if not userIsGroupAdmin(request, group):
            return responseJsonUtil(False, 'ERROR303',  None)

        tmpDate = getPropertyByName("date",request.QUERY_PARAMS.items())
        tmpResultLogs = Log.objects.raw('select * from main_log where user_id = '+str(getUserByRequest(request).id)+' and group_id = ' + group+' and date ="'+tmpDate+'"')
        tmpSerializer = LogSerializer(tmpResultLogs)
        return responseJsonUtil(True, None, tmpSerializer)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        tmpActivities = getPropertyByName('activities', data.items())
        tmpGroup = getPropertyByName('group', data.items())
        tmpDate = getPropertyByName('date', data.items())

        with transaction.commit_on_success():
            deleteLog(getUserByRequest(request).id, tmpGroup, tmpDate)
            for tmpObject in tmpActivities:
                tmpErrorName = validateProject(request, getPropertyByName('project', tmpObject.items()), getPropertyByName('group', tmpObject.items()))
                if tmpErrorName:
                    transaction.rollback()
                    return responseJsonUtil(False, tmpErrorName,  None)
                tmpLog = logDeserializer(tmpObject)
                tmpLog.save()
            return responseJsonUtil(True, None, None)
        return responseJsonUtil(False, None, None)


def deleteLog(argUser, argGroup, argDate):
    Log.objects.filter(user=argUser, group=Group.objects.get(pk=argGroup), date=argDate).update(entity_status=1)


def validateProject(request, argProjectID, argGroupID):
    if not groupExists(argGroupID):
        return 'ERROR200'
    if not userIsGroupMember(request, argGroupID):
        return 'ERROR304'
    if not projectExists(argProjectID):
        return 'ERROR500'
    if not userIsProjectMember(request, argProjectID):
        return 'ERROR305'
    return None


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
                return responseJsonUtil(False, errorCode, None)
            reportBook = buildReport(tmpGroupID, tmpProjectID, tmpUserID,tmpDateRangeId,tmpStartDate,tmpEndDate)
            return buildExcelFileResponse('logReport.xls', reportBook)
    else:
        return responseJsonUtil(False, 'ERROR100', None)


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

