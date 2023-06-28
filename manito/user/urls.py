from django.contrib import admin
from django.urls import path, include

from user.views import RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
]
