from django.urls import path

from user.views import RegisterAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("signin/", LoginAPIView.as_view()),
    path("signout/", LogoutAPIView.as_view())
]
