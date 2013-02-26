from django.http import HttpResponse
import json

def responseUtil(argSuccess, argErrorCode, argResult):
    return HttpResponse(json.dumps({'success': argSuccess, 'error': argErrorCode, 'result': argResult.data}),
                        content_type='application/json')