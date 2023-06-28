from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from manito.models import Manito
from partner.models import Partner
from partner.serializers import PartnerSerializer


# TODO: Permission 적용
class PartnerListAPIView(ListAPIView):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        manito_id = self.kwargs['manito_id']
        return Partner.objects.filter(manito_id=manito_id)

    def get(self, request, *args, **kwargs):
        manito_id = self.kwargs['manito_id']
        try:
            manito = Manito.objects.get(id=manito_id)
            print(manito.end_at)
            print(timezone.now())
            if manito.type == 'A' and manito.end_at > timezone.now():
                return Response({"error: 아직은 비밀이에요!"}, status=401)
        except:
            return super().get(request, *args, **kwargs)
