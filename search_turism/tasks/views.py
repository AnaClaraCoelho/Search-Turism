# coding: utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import todo_svc


@csrf_exempt
@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(
        request.POST.get("city"),
        request.POST.get("touristSpot"),
        request.POST.get("description"),
        request.POST.get("url_image")
        )
    return JsonResponse(todo)

def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({"todos": todos})

@ajax_login_required
def delete_todo(request):
    todo = todo_svc.delete_todo(
        json.loads(request.body.decode())
    )
    return JsonResponse(todo, safe=False)

@ajax_login_required
def edit_todo(request):
    todo = todo_svc.edit_todo(
        json.loads(request.body.decode())
    )
    return JsonResponse(todo, safe=False)

