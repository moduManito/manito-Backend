from rest_framework.response import Response
from rest_framework.views import APIView

from partner.models import Partner


# TODO: Permission 적용
class PartnerCountView(APIView):
    """
    현재까지 탄생한 마니또 수 반환
    """

    def get(self, request):
        total_count = Partner.objects.count()
        data = {
            "total_count": total_count
        }
        return Response(data)
