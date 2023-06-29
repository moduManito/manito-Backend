from django.utils import timezone
from django.utils.timezone import localtime
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from manito.models import Manito
from partner.models import Partner
from partner.permissions import IsManitoOwner
from partner.serializers import PartnerSerializer


# TODO: Permission 적용
class PartnerListAPIView(ListAPIView):
    serializer_class = PartnerSerializer
    permission_classes = [IsManitoOwner]

    def get_queryset(self):
        manito_id = self.kwargs['manito_id']
        return Partner.objects.filter(manito_id=manito_id)

    def get(self, request, *args, **kwargs):
        manito_id = self.kwargs['manito_id']
        manito = Manito.objects.get(id=manito_id)
        partners = Partner.objects.filter(manito_id=manito_id)
        manito_sender = []
        manito_receiver = []

        for partner in partners:
            manito_sender.append(partner.manito_sender)
            manito_receiver.append(partner.manito_receiver)

        res_data = {
            "title": manito.title,
            "created_at": localtime(manito.created_at).strftime(
                "%Y-%m-%d %H:%M:%S"),
            "end_at": localtime(manito.end_at).strftime("%Y-%m-%d %H:%M:%S"),
            "manito_sender": manito_sender,
            "manito_receiver": manito_receiver,
        }

        if manito is None:
            return Response({"error: 존재하지 않는 페이지 입니다."}, status=404)
        if manito.type == 'A' and manito.end_at > timezone.now():
            return Response({"error: 아직은 비밀이에요!"}, status=401)
        return Response(res_data, status=200)
