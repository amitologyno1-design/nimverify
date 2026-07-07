from django.urls import path
from . import views

urlpatterns = [
    path("", views.verify_nin, name="verify_nin"),
]