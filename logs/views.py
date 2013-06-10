from main.models import Log, Group, Note
from main.utils import *
from logs.logReports import *
from logs.serializers import *
from logs.deserializers import *
from django.db import transaction
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.db import connection

@api_view(['GET','POST', 'DELETE'])
def myLogsServices(request, group, argLog, format=None):

    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR103',  None)

    if request.method == 'DELETE':
        if not logExists(argLog):
            return responseJsonUtil(False, 'ERROR700',  None)
        Log.objects.filter(pk=argLog).update(entity_status=1)
        return responseJsonUtil(True, None, None)

    if request.method == 'GET':
        if not groupExists(group):
            return responseJsonUtil(False, 'ERROR200',  None)
        tmpDate = getPropertyByName("date",request.QUERY_PARAMS.items())
        if not tmpDate:
            return responseJsonUtil(False, 'ERROR800',  None)
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
        tmpUser = getUserByRequest(request)

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


@api_view(['POST'])
def create_log(request, format=None):
    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR103',  None)

    try:
        tmpData = JSONParser().parse(request)
        tmpUser = getUserByRequest(request)
        tmpDate = convertDateFromDatePicker(getPropertyByName('date', tmpData.items()))
        tmpLog = logDeserializer(tmpData, tmpUser, tmpDate)
        tmpLog.save()
        tmpSerializer = LogSerializer(tmpLog)
        return responseJsonUtil(True, None, tmpSerializer)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)


@api_view(['PUT'])
def update_log(request, pk, format=None):
    try:
        log = Log.objects.get(pk=pk)
    except Log.DoesNotExist:
        return responseJsonUtil(False, 404, None)
    data = JSONParser().parse(request)
    tmpNotes = getPropertyByName('notes', data.items())

    with transaction.commit_on_success():
        for tmpObject in tmpNotes:
            tmpId = getPropertyByName('id', tmpObject.items())
            tmpAction = getPropertyByName('action', tmpObject.items())
            if tmpAction == 1:
                tmpNote = Note.objects.get(pk=getPropertyByName('id', tmpObject.items()))
                tmpNote.note = getPropertyByName('note', tmpObject.items())
                tmpNote.save()
            if tmpId == 0:
                tmpNote = noteDeserializer(tmpObject)
                tmpNote.save()

    Log.objects.filter(id=getPropertyByName('id', data.items())).update(
        activity=getPropertyByName('activity', data.items()),
        time=getPropertyByName('time', data.items()),
        project=Project.objects.get(pk=getPropertyByName('project', data.items())))
    tmpLog = Log.objects.get(pk=pk)
    tmpSerializer = LogSerializer(tmpLog)
    return responseJsonUtil(True, None, tmpSerializer)


def deleteLog(argUser, argGroup, argDate):
    Log.objects.filter(user=argUser, group=Group.objects.get(pk=argGroup), date=argDate).update(entity_status=1)


@api_view(['DELETE'])
def delete_note(request, pk, format=None):
    try:
        Note.objects.filter(id=pk).update(entity_status=1)
        return responseJsonUtil(True, None, None)
    except BaseException:
        return responseJsonUtil(False, 'ERROR000', None)


@api_view(['GET'])
def get_notes(request, log, format=None):
    tmpResultNotes = Note.objects.raw('select id , note, log_id as activity from main_note where log_id = ' + log + ' and entity_status=0')
    tmpSerializer = NoteSerializer(tmpResultNotes)
    return responseJsonUtil(True, None, tmpSerializer)


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


def validateExportReport(request):
    data = request.DATA
    if not groupExists(getPropertyByName('group',data.items())):
        return 'ERROR200'
    return None

@api_view(['POST','GET', 'PUT'])
def exportReport(request, format=None):
    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR103', None)
    if request.method == 'POST':
        if validateExportReport(request):
            return responseJsonUtil(False, validateExportReport(request),  None)
        return responseJsonUtil(True, None, None);
    if request.method == 'PUT':
        if validateExportReport(request):
            return responseJsonUtil(False, validateExportReport(request),  None)
        return responseJsonUtil(True, None, None);
    if request.method == 'GET':
        data = request.QUERY_PARAMS
        tmpGroupID = getPropertyByName('group',data.items())
        tmpProjectID = getPropertyByName('project',data.items())
        tmpUserID = getPropertyByName('user',data.items())
        tmpDateRangeId = getPropertyByName('dateRangeOption',data.items())
        tmpStartDate = convertDateFromDatePicker(getPropertyByName('startDate',data.items()))
        tmpEndDate = convertDateFromDatePicker(getPropertyByName('endDate',data.items()))
        errorCode = exportReportPermissionsValidation(tmpGroupID)
        if errorCode != None:
            return responseJsonUtil(False, errorCode, None)
        reportBook = buildReport(tmpGroupID, tmpProjectID, tmpUserID,tmpDateRangeId,tmpStartDate,tmpEndDate)
        return buildExcelFileResponse('logReport.xls', reportBook)


@api_view(['GET'])
def listReport(request, group, project, user, range):
    if not userAuthentication(request):
        return responseJsonUtil(False, 'ERROR103', None)
    if request.method == 'GET':
        errorCode = exportReportPermissionsValidation(group)
        if errorCode != None:
            return responseJsonUtil(False, errorCode, None)
        data = request.QUERY_PARAMS
        tmpStartDate = convertDateFromDatePicker(getPropertyByName('startDate',data.items()))
        tmpEndDate = convertDateFromDatePicker(getPropertyByName('endDate',data.items()))
        tmpResultLogs = getListReport(group, project, user, range, tmpStartDate, tmpEndDate)
        tmpSerializer = LogGroupProjectDateDTOSerializer(tmpResultLogs)
        return responseJsonUtil(True, None, tmpSerializer)


def exportReportPermissionsValidation(argGroupID):
    try:
        Group.objects.get(id = argGroupID)
    except:
        return 'ERROR200'
    return None


@api_view(['POST', 'PUT'])
def sendStatus(request, format=None):
    data = JSONParser().parse(request)
    cursor = connection.cursor()
    tmpUser = User.objects.get(email=getPropertyByName('email', data.items()))
    tmpUserId = tmpUser.id
    tmpDate = convertDateFromDatePicker(getPropertyByName('date', data.items()))
    cursor.execute('select distinct project_id from main_log where date =\'' + tmpDate + '\'' + ' and user_id =' + str(tmpUserId) + ' and entity_status=0')
    for row in cursor.fetchall():
        tmpAdminEmails = []
        tmpLogs = []
        tmpProjectId = row[0]
        cursor.execute('select email from main_project mproject, main_project_user mprojectuser, main_user muser '
                       'where mproject.id = mprojectuser.project_id and mprojectuser.user_id = muser.id '
                       'and mproject.id=' + str(tmpProjectId) + ' and mprojectuser.role_id = 1')
        for row in cursor.fetchall():
            tmpAdminEmails.insert(0,row[0])
        cursor.execute('select activity, log.time, log.date, project.name as project_name, log.id '
                       'from main_log log inner join main_project project on log.project_id = project.id '
                       'where log.entity_status=0 and log.user_id =' + str(tmpUserId) + ' and '
                       'log.date =\'' + tmpDate + '\'' + ' and project_id = ' + str(tmpProjectId))
        for row in cursor.fetchall():
            tmpLogs.insert(0,row)
        user_email = getPropertyByName('email', data.items())
        if emailExists(user_email):
            code = md5Encoding(tokenGenerator())
            FROM = user_email
            activities = ""
            for item in tmpLogs:
                cursor.execute('select note from main_note where log_id =' + str(item[4]) + ' and entity_status = 0')
                notes = ""
                for row in cursor.fetchall():
                    notes += row[0] + '\n'
                activities += '\n'"""Task: """ + item[0] + '\n' """Time: """ + str(item[1]) + """ hours""" '\n' + """Notes: """ + notes +'\n'
            SUBJECT = "Status " + item[3] + " Date: " + str(item[2])
            MESSAGE = """
            There is my status:
                """ + activities + """

            Thanks"""
            try:
                tmpUser = User.objects.get(email=user_email)
            except:
                return responseJsonUtil(False, 'ERROR000', None)
            try:
                sendEmail(user_email, tmpAdminEmails, SUBJECT, MESSAGE)
            except:
                return responseJsonUtil(False, 'ERROR002', None)
        else:
            return responseJsonUtil(False, 'ERROR102', None)
    return responseJsonUtil(True, None, None)

