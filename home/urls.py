from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", lambda request: redirect("register")),
    path("login/", lambda request: redirect("login")),
]