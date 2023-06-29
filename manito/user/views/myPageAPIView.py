from rest_framework.response import Response
from rest_framework.views import APIView

from manito.models import Manito
from manito.serializers import AbstractManitoSerializer


class MyPageAPIView(APIView):

    def get(self, request):
        user = request.user
        manito = Manito.objects.filter(author=user)
        serializer = AbstractManitoSerializer(manito, many=True)
        return Response(serializer.data)
