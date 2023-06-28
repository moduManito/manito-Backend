import random
import re
import smtplib
from email.mime.text import MIMEText

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from manito.models import Manito
from manito.serializers.manitoSerializers import ManitoSerializer
from partner.models import Partner
from user.models import User


# Create your views here.

def sendEmail(name_data, mail_data, price):
    s = smtplib.SMTP('smtp.gmail.com', 587)  # 세션 생성
    s.starttls()  # TLS 보안 시작
    s.login('modumanito@gmail.com', 'llzywzvdxeyjfhre')  # 로그인 인증
    # 마니또 받는 사람 
    # 프론트에서 받아야하는 데이터
    manito_sender = [name.strip() for name in name_data[1:-1].split(',')]
    manito_mail = [email.strip() for email in mail_data[1:-1].split(',')]
    shuffle_manito = [name.strip() for name in name_data[1:-1].split(',')]

    # 중복 제거 처리
    while True:
        flag = True
        random.shuffle(shuffle_manito)
        for i in range(len(manito_sender)):
            # 동일요소가 있다면 다시 셔플 진행
            if manito_sender[i] == shuffle_manito[i]:
                flag = False
                break
                # 중복이 없다면 flag는 True
        if flag:
            break

    for i in range(len(manito_sender)):
        # for i in range(len('a')):
        msg = MIMEText(
            f'안녕하세요! {manito_sender[i]}님!! \n 당신의 마니또는 {shuffle_manito[i]}입니다! 예산은 {price}원이며 마니또의 선물을 준비해주세요!')
        msg['Subject'] = '모두의 마니또'
        s.sendmail("modumanito@gmail.com", f"{manito_mail[i]}", msg.as_string())

    s.quit()  # 세션 종료

    return manito_sender, shuffle_manito, manito_mail


class ManitoAPI(CreateAPIView):
    queryset = Manito.objects.all()
    serializer_class = ManitoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        manito_sender, manito_receiver, manito_mail = sendEmail(
            serializer.validated_data['name_data'],
            serializer.validated_data['mail_data'],
            serializer.validated_data['price'])
        self.perform_create(serializer)
        manito = serializer.instance
        for i in range(len(manito_receiver)):
            Partner.objects.create(
                manito=manito,
                manito_sender=manito_sender[i],
                manito_receiver=manito_receiver[i]
            )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
