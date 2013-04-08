from main.models import Log, Group
from main.utils import *
from logs.logReports import *
from logs.serializers import LogGroupProjectDateDTOSerializer
from logs.deserializers import logDeserializer
from logs.dtos import LogGroupProjectDateDTO
from django.db import connection
from django.db import transaction
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def myLogsServices(request, group, format=None):

    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR103',  None)

    if request.method == 'GET':
        if not groupExists(group):
            return responseJsonUtil(False, 'ERROR200',  None)
        if not userIsGroupAdmin(request, group):
            return responseJsonUtil(False, 'ERROR303',  None)
        tmpDate = getPropertyByName("date",request.QUERY_PARAMS.items())
        tmpResultLogs = Log.objects.raw('select log.id , activity, log.time, log.date, log.user_id, project.id as project_id, project.name as project_name, log.group_id '
                                        'from main_log log inner join main_project project on log.project_id = project.id '
                                        'where log.entity_status=0 and log.user_id = '+str(getUserByRequest(request).id)+' and log.group_id = '+group+' and log.date =\''+tmpDate+'\'')
        tmpSerializer = LogGroupProjectDateDTOSerializer(tmpResultLogs)
        return responseJsonUtil(True, None, tmpSerializer)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        tmpActivities = getPropertyByName('activities', data.items())
        tmpGroup = getPropertyByName('group', data.items())
        tmpDate = convertDateFromDatePicker(getPropertyByName('date', data.items()))
        tmpUser = getUserByRequest(request);

        with transaction.commit_on_success():
            deleteLog(getUserByRequest(request).id, tmpGroup, tmpDate)
            for tmpObject in tmpActivities:
                tmpErrorName = validateProject(request, getPropertyByName('project', tmpObject.items()), getPropertyByName('group', tmpObject.items()))
                if tmpErrorName:
                    transaction.rollback()
                    return responseJsonUtil(False, tmpErrorName,  None)
                tmpLog = logDeserializer(tmpObject, tmpUser, tmpDate)
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
        return responseJsonUtil(False, 'ERROR103', None)


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

