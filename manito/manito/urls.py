from django.urls import path, include
from manito.views import ManitoCreateAPIView
from partner.views import PartnerCountView
from manito.views import ManitoCheckAPIView

app_name = "manito"

urlpatterns = [
    path("", ManitoCreateAPIView.as_view()),
    path("<int:manito_id>/partner/", include('partner.urls')),
    path("count/", PartnerCountView.as_view()),
    path("<int:manito_id>/check/", ManitoCheckAPIView.as_view())
]
