from rest_framework.response import Response
from rest_framework.views import APIView

from manito.models import Manito
from manito.serializers import AbstractManitoSerializer


class MyPageAPIView(APIView):

    def get(self, request):
        """
        내가 만든 마니또 목록 및 유저 데이터 반환
        """
        user = request.user
        if user.is_anonymous:
            return Response({"error": "로그인이 필요합니다."}, status=401)
        manito = Manito.objects.filter(author=user)
        serializer = AbstractManitoSerializer(manito, many=True)
        return Response(serializer.data)
