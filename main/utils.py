from main.models import User
from rest_framework.response import Response


# Format a response that returns an json with the following properties:
# success Boolean
# error String
# Collection of data
def responseJsonUtil(argSuccess, argErrorCode, argResult):
    if argResult == None:
        return Response({'success': argSuccess, 'error': argErrorCode, 'result': argResult})
    else:
        return Response({'success': argSuccess, 'error': argErrorCode, 'result': argResult.data})


# Validate if the user exists in DB
def userAuthentication(request):
    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        tmpUser = User.objects.get(password=tmpPassword,email=tmpMail,entity_status=0)
        return True;
    except User.DoesNotExist:
        return False;

# The format string which returns is ej: September 24 2010 17:03
def dateToString(argDate):
    return argDate.strftime('%B %d %Y %H:%M')


# The format string which returns is ej: September 24 2010 17:03
def stringToDate(argString):
    return argString.strptime('%B %d %Y %H:%M')


# Retrieve a desired value from a List in a key-value format
def getPropertyByName(argProperty,argData):

    for key, value in argData:
        if argProperty==key:
            return value