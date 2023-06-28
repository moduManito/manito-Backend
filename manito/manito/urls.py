from django.urls import path
from manito.views import ManitoAPI

urlpatterns = [
    path("", ManitoAPI.as_view())
]