from django.http import HttpResponse
from main.models import User
import json


def responseUtil(argSuccess, argErrorCode, argResult):
    return HttpResponse(json.dumps({'success': argSuccess, 'error': argErrorCode, 'result': argResult.data}),
                        content_type='application/json')


def userAuthentication(argMail, argPassword):
    try:
        tmpUser = User.objects.get(password=argPassword,email=argMail,entity_status=0)
        return True;
    except User.DoesNotExist:
        return False;