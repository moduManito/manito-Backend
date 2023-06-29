from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                return Response({"message": "로그아웃 성공"},
                                status=200)
            except Exception:
                return Response({"message": "유효하지 않은 토큰입니다."},
                                status=400)
        else:
            return Response({"message": "Refresh 토큰이 필요합니다."},
                            status=400)
