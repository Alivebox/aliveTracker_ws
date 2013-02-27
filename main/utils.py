from django.http import HttpResponse
from main.models import User

import json


# Format a response that returns an json with the following properties:
# success Boolean
# error String
# Collection of data
def responseJsonUtil(argSuccess, argErrorCode, argResult):
    return HttpResponse(json.dumps({'success': argSuccess, 'error': argErrorCode, 'result': argResult.data}),
                        content_type='application/json')


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