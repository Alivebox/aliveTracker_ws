from django.contrib.sessions.models import Session
from main.models import *
from rest_framework.response import Response
from datetime import datetime
import string, datetime, smtplib, random, hashlib


# Format a response that returns an json with the following properties:
# success Boolean
# error String
# Collection of data
def responseJsonUtil(argSuccess, argErrorCode, argResult):
    if argResult is None:
        return Response({'success': argSuccess, 'error': argErrorCode, 'result': argResult})
    else:
        return Response({'success': argSuccess, 'error': argErrorCode, 'result': argResult.data})


# Build a Json Response with raw JSON element as argRawResult
def rawResponseJsonUtil(argSuccess, argErrorCode, argRawResult):
    if argRawResult is None:
        return Response({'success': argSuccess, 'error': argErrorCode, 'result': argRawResult})
    else:
        return Response({'success': argSuccess, 'error': argErrorCode, 'result': argRawResult})


# Validate if the user exists in DB
def userAuthentication(argRequest):
    try:
        tmpSession = Session.objects.get(session_key=argRequest.session._session_key)
        if tmpSession.expire_date.date() < datetime.datetime.now().date():
            return False
        return True
    except Session.DoesNotExist:
        return False


# return user filtering by request information
def getUserByRequest(argRequest):
    try:
        tmpUser = User.objects.get(session_key=argRequest.session._session_key)
        return tmpUser
    except User.DoesNotExist:
        return None


def getAdminRole():
    try:
        tmpRole = Role.objects.get(pk=1)
        return tmpRole
    except User.DoesNotExist:
        return None

# The format string which returns is ej: September 24 2010 17:03
def dateToString(argDate):
    return argDate.strftime('%B %d %Y %H:%M')


# The format string which returns is ej: September 24 2010 17:03
def stringToDate(argString):
    return argString.strptime('%B %d %Y %H:%M')


# Retrieve a desired value from a List in a key-value format
def getPropertyByName(argProperty, argData):

    for key, value in argData:
        if argProperty == key:
            return value


# Sends email with the specified data
def sendEmail(argFROM, argTO, argSUBJECT, argMESSAGE):

    BODY = string.join((
                           "From: %s" % argFROM,
                           "Date: %s" % datetime.datetime.now(),
                           "To: %s" % argTO,
                           "Subject: %s" % argSUBJECT ,
                           "",
                           argMESSAGE
                       ), "\r\n")
    try:
        server = smtplib.SMTP('mail.alivebox.com')
        server.sendmail(argFROM, argTO, BODY)
        return True
    except:
        return False


# Generates a random alfanumeric token of the specified size
def tokenGenerator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


#Encode the argString to MD5
def md5Encoding(argString):
    code = hashlib.md5()
    code.update(argString)
    return code.hexdigest()


# Validate if the email exists in DB
def emailExists(argEmail):
    try:
        tmpUser = User.objects.get(email=argEmail)
        return True
    except User.DoesNotExist:
        return False


#
# Validate if the email and token exists in DB
def correctForgotPasswordToken(argEmail, argToken):
    try:
        tmpUser = User.objects.get(email=argEmail)
        User_Forgot_Password.objects.get(user=tmpUser, token=argToken)
        return True
    except User_Forgot_Password.DoesNotExist:
        return False


# Validate if the group exists in DB
def groupExists(argGroupID):
    try:
        Group.objects.get(id=argGroupID)
        return True
    except Group.DoesNotExist:
        return False

# Validate if the project exists in DB
def projectExists(argProjectID):
    try:
        Project.objects.get(id=argProjectID)
        return True
    except Project.DoesNotExist:
        return False


# Validate if the user is group manager
def userIsGroupAdmin(argRequest, argGroupID):
    try:
        tmpUser = getUserByRequest(argRequest)
        tmpGroup = Group.objects.get(id=argGroupID)
        tmpRole = Role.objects.get(id=1)
        Group_User.objects.get(user=tmpUser,group=tmpGroup,role=tmpRole)
        return True
    except Group_User.DoesNotExist:
        return False


# Validate if the user is group member
def userIsGroupMember(argRequest, argGroupID):
    try:
        tmpUser = getUserByRequest(argRequest)
        tmpGroup = Group.objects.get(id=argGroupID)
        Group_User.objects.get(user=tmpUser,group=tmpGroup)
        return True
    except Group_User.DoesNotExist:
        return False


# Validate if the user is Project member
def userIsProjectMember(argRequest, argProjectID):
    try:
        tmpUser = getUserByRequest(argRequest)
        tmpProject = Group.objects.get(id=argProjectID)
        Project_User.objects.get(user=tmpUser,project=tmpProject)
        return True
    except Project_User.DoesNotExist:
        return False


# Validate if the user is Project member
def userIsProjectMember(argRequest, argProjectID):
    try:
        tmpUser = getUserByRequest(argRequest)
        tmpProject = Project.objects.get(id=argProjectID)
        Project_User.objects.get(user=tmpUser,project=tmpProject)
        return True
    except Project_User.DoesNotExist:
        return False

def convertDateFromDatePicker(argStringDate):
    tmpCleanString = argStringDate[:10]
    return tmpCleanString