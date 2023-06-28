from django.urls import path, include
from manito.views import ManitoCreateAPIView
from partner.views import PartnerCountView

app_name = "manito"

urlpatterns = [
    path("", ManitoCreateAPIView.as_view()),
    path("<int:manito_id>/partner/", include('partner.urls')),
    path("count/", PartnerCountView.as_view()),
]
