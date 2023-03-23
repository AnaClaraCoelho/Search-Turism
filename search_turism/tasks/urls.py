from django.urls import path

from . import views

urlpatterns = [
    path("add", views.add_todo),
    path("list", views.list_todos),
    path("delete", views.delete_todo),
    path("edit", views.edit_todo),
    path("like", views.add_like),
    path("unlike", views.remove_like),
]
