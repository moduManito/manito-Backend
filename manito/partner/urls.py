from django.urls import path

from partner.views import PartnerListAPIView, PartnerCountView

urlpatterns = [
    path('', PartnerListAPIView.as_view()),
]
