from main.models import Log, User
from django.http import HttpResponse
from xlwt import Workbook, XFStyle, Font


def buildExcelFileResponse(argFileName, argWorkBook):
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % argFileName
    argWorkBook.save(response)
    return response


def addReportSheet(argWorkBook, argUserName, argLogDetail):
    headerStyle = defineFontStyle('Times New Roman',True)
    rowStyle = defineFontStyle('Times New Roman',False)
    reportSheet = argWorkBook.add_sheet(argUserName)
    if len(list(argLogDetail)) > 0:
        defineSheetHeader(reportSheet,headerStyle)
        index = 0
        for value in argLogDetail:
            index += 1
            addSheetRow(reportSheet,index,value, argUserName,rowStyle)
    else:
        defineVoidActivitySheet(reportSheet,headerStyle)


def defineFontStyle(argFontName,argIsBold):
    style = XFStyle()
    font = Font()
    font.name = argFontName
    font.bold = argIsBold
    style.font = font
    return style


def defineSheetHeader(argReportSheet,argHeaderStyle):
    argReportSheet.write(0, 0, 'Project',argHeaderStyle)
    argReportSheet.write(0, 1, 'User',argHeaderStyle)
    argReportSheet.write(0, 2, 'Activity',argHeaderStyle)
    argReportSheet.write(0, 3, 'Time',argHeaderStyle)
    argReportSheet.write(0, 4, 'Date',argHeaderStyle)


def defineVoidActivitySheet(argReportSheet,argHeaderStyle):
    argReportSheet.write(0, 0, 'The user does not register any activity in the given period of time',argHeaderStyle)


def addSheetRow(argReportSheet,argIndex,argValue, argUserName, argHeaderStyle):
    argReportSheet.write(argIndex, 0, str(argValue.project_name),argHeaderStyle)
    argReportSheet.write(argIndex, 1, str(argUserName),argHeaderStyle)
    argReportSheet.write(argIndex, 2, str(argValue.activity),argHeaderStyle)
    argReportSheet.write(argIndex, 3, str(argValue.time),argHeaderStyle)
    argReportSheet.write(argIndex, 4, str(argValue.date),argHeaderStyle)


def buildReport(argGroupID,argProjectID,argUserID, argRangeId, argStartDate=None, argEndDate=None):
    reportBook = Workbook()
    if argUserID!='0':
        tmpUser = User.objects.get(id = argUserID)
        reportBook = addUserReportSheet(reportBook,argGroupID,argProjectID,tmpUser,argRangeId, argStartDate, argEndDate)
    else:
        if argUserID =='0' and argProjectID=='0':
            query= 'select * from main_user where id in ( select user_id from main_group_user where group_id='+str(argGroupID)+' ) and entity_status <> 1'
        else:
            query= 'select * from main_user where id in ( select user_id from main_project_user where project_id='+str(argProjectID)+' ) and entity_status <> 1'
        tmpUsers = User.objects.raw(query)
        for value in tmpUsers:
            reportBook = addUserReportSheet(reportBook,argGroupID,argProjectID,value,argRangeId, argStartDate, argEndDate)
    return reportBook


def getListReport(argGroupID,argProjectID,argUserID, argRangeId, argStartDate=None, argEndDate=None):
    tmpQuery = buildReportQuery(argGroupID,argProjectID,argUserID,argRangeId, argStartDate, argEndDate)
    tmpLogsRegister = Log.objects.raw(tmpQuery)
    return tmpLogsRegister


def addUserReportSheet(reportBook,argGroupID,argProjectID,argUser, argRangeId, argStartDate=None, argEndDate=None):
    tmpQuery = buildReportQuery(argGroupID,argProjectID,argUser.id,argRangeId, argStartDate, argEndDate)
    logsRegister = Log.objects.raw(tmpQuery)
    if argUser.name == '':
        addReportSheet(reportBook, argUser.email, logsRegister)
    else:
        addReportSheet(reportBook, argUser.name, logsRegister)
    return reportBook

def buildReportQuery(argGroupID,argProjectID,argUserID, argRangeId, argStartDate=None, argEndDate=None):
    tmpFilter = "select log.id , activity, log.time, log.date, project.name as project_name from " \
                "main_log log inner join main_project project on log.project_id = project.id " \
                "where project.entity_status = 0 and log.group_id = "+str(argGroupID)
    if argUserID != '0':
        tmpFilter = tmpFilter +" and  log.user_id = "+ str(argUserID)
    if argProjectID != '0':
        tmpFilter = tmpFilter +" and  project_id = "+ str(argProjectID)
    if argRangeId == '0':
        tmpFilter = tmpFilter +" and date between '"+str(argStartDate)+"' and '"+str(argEndDate)+"'"
    else:
        if argRangeId == '1':
            tmpFilter = tmpFilter +" and date between DATE_SUB(CURRENT_DATE,INTERVAL 1 DAY) and CURRENT_DATE"
        if argRangeId == '2':
            tmpFilter = tmpFilter +" and date between DATE_SUB(CURRENT_DATE,INTERVAL 7 DAY) and CURRENT_DATE"
        if argRangeId == '3':
            tmpFilter = tmpFilter +" and date between DATE_SUB(CURRENT_DATE,INTERVAL 14 DAY) and CURRENT_DATE"
        if argRangeId == '4':
            tmpFilter = tmpFilter +" and date between DATE_SUB(CURRENT_DATE,INTERVAL 30 DAY) and CURRENT_DATE"
    return tmpFilter+" and log.entity_status = 0 order by project_id, date asc"


