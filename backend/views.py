import json

from django.core import serializers
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.http import require_http_methods

from backend.models import User


@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = User(username=request.GET.get('username'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        user = User.objects.filter()
        response['list']  =json.loads(serializers.serialize("json",user))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = 'error'
        response['error_num'] = 1
    return JsonResponse(response)
