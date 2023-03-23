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
    id = request.POST.get('id')
    city = request.POST.get('city')
    tourist_spot = request.POST.get('tourist_spot')
    description = request.POST.get('description')
    url_image = request.POST.get('url_image')
    todo_svc.edit_todo(id, city, tourist_spot, description, url_image)


def liked(request):
    id = request.GET.get("id")
    todo_svc.liked(id)
