from rest_framework import status
from rest_framework.views import APIView
from .serializers.manitoSerializers import ManitoSerializer
from rest_framework.response import Response
import smtplib
import random
from email.mime.text import MIMEText

# Create your views here.

def sendEmail(name_data, mail_data, price):
    s = smtplib.SMTP('smtp.gmail.com', 587) # 세션 생성
    s.starttls() # TLS 보안 시작
    s.login('modumanito@gmail.com', 'llzywzvdxeyjfhre') # 로그인 인증
    # 마니또 받는 사람 
    # 프론트에서 받아야하는 데이터
    manito_receiver = name_data
    manito_mail = mail_data
    shuffle_manito = name_data

    # 중복 제거 처리 
    while True :
        flag = True 
        random.shuffle(shuffle_manito)
        for i in range(len(manito_receiver)):
            # 동일요소가 있다면 다시 셔플 진행 
            if manito_receiver[i] == shuffle_manito[i]:
                flag = False 
                break 
        # 중복이 없다면 flag는 True 
        if flag:
            break

    for i in range(len(manito_receiver)):
    # for i in range(len('a')):
        msg = MIMEText(f'안녕하세요! {manito_receiver[i]}님!! \n 당신의 마니또는 {shuffle_manito[i]}입니다! 예산은 {price}원이며 마니또의 선물을 준비해주세요!')
        msg['Subject'] = '모두의 마니또'
        s.sendmail("modumanito@gmail.com", f"{manito_mail[i]}", msg.as_string())
        # s.sendmail("modumanito@gmail.com", "rayleigh190@gmail.com", msg.as_string())

    s.quit() # 세션 종료
    

class ManitoAPI(APIView):
    def post(self, request):
        serializer = ManitoSerializer(data=request.data)
        if serializer.is_valid():
            # sendEmail(serializer.validated_data['name_data'], serializer.validated_data['mail_data'], serializer.validated_data['price'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
