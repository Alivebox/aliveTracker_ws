from django.http import HttpResponse
from main.models import User
import json


def responseJsonUtil(argSuccess, argErrorCode, argResult):
    return HttpResponse(json.dumps({'success': argSuccess, 'error': argErrorCode, 'result': argResult.data}),
                        content_type='application/json')


def userAuthentication(request):
    try:
        tmpMail = request.META['HTTP_USERNAME']
        tmpPassword = request.META['HTTP_PASSWORD']
        tmpUser = User.objects.get(password=tmpPassword,email=tmpMail,entity_status=0)
        return True;
    except User.DoesNotExist:
        return False;