# coding: utf-8
import json
from django.http import JsonResponse
from django.contrib import auth
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from ..tasks.service import log_svc

@csrf_exempt
def register(request):
    if request.method == 'POST':
        input_user= json.loads(request.body)
        username = input_user.get("username")
        email = input_user.get("email")
        password = input_user.get("password")
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email já está sendo usado.'})
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Nome de usuário já existe.'})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return JsonResponse({'success': 'Usuer created'})
    return JsonResponse({'error': 'Wrong method'})

        

@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return JsonResponse({})


def whoami(request):
    i_am = (
        {
            "user": _user2dict(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    return JsonResponse(i_am)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }
    return d
