from rest_framework.generics import ListAPIView

from partner.models import Partner
from partner.serializers import PartnerSerializer


# TODO: Permission 적용
class PartnerListAPIView(ListAPIView):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        manito_id = self.kwargs['manito_id']
        return Partner.objects.filter(manito_id=manito_id)
