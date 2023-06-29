import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from manito.models import Manito
from manito.serializers.manitoSerializers import ManitoSerializer
from partner.models import Partner

admin_mail = os.environ.get("ADMIN_EMAIL")
admin_password = os.environ.get("ADMIN_PASSWORD")


def sendEmail(name_data, mail_data, price, title, content, author):
    title = title
    content = content
    price = price
    author = author

    s = smtplib.SMTP('smtp.gmail.com', 587)  # 세션 생성
    s.starttls()  # TLS 보안 시작
    s.login(admin_mail, admin_password)  # 로그인 인증
    # 마니또 받는 사람 
    # 프론트에서 받아야하는 데이터
    manito_sender = [name.strip() for name in name_data.split(',')]
    manito_mail = [email.strip() for email in mail_data.split(',')]
    shuffle_manito = [name.strip() for name in name_data.split(',')]
    if len(manito_sender) <= 1:
        return manito_sender, shuffle_manito, manito_mail

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

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = '모두의 마니또'
        msg = MIMEMultipart('alternative')
        msgRoot.attach(msg)

        msg_html = f'''
        <img style="width: 200px;" src="https://github.com/Rayleigh190/Orange/assets/86937253/168590d0-1429-4088-9926-a931f4382690"/>
        <h1>🎊 {title} 마니또에 초대 됐습니다!{author} 🎉</h1>
        <p>안녕하세요👋 {manito_sender[i]}님!!</p>
        <p> 당신의 마니또는 {shuffle_manito[i]}입니다! 💰예산은 {price}원이며 마니또의 🎁선물을 준비해주세요!</p><br/>
        <div style='background-color: #EBEBEB; padding: 8px; width: 450px'>📢 {content}</div>
        '''

        msg_body = MIMEText(msg_html, 'html')
        msg.attach(msg_body)

        try:
            s.sendmail(admin_mail, f"{manito_mail[i]}", msgRoot.as_string())
        except Exception as e:
            print("err: ", str(e))

    s.quit()  # 세션 종료

    return manito_sender, shuffle_manito, manito_mail


def sendCheckEmail(mail_data, author):
    s = smtplib.SMTP('smtp.gmail.com', 587)  # 세션 생성
    s.starttls()  # TLS 보안 시작
    s.login(admin_mail, admin_password)  # 로그인 인증
    # 마니또 받는 사람 
    manito_mail = [email.strip() for email in mail_data[1:-1].split(',')]

    for i in range(len(manito_mail)):
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = '모두의 마니또'
        msg = MIMEMultipart('alternative')
        msgRoot.attach(msg)

        msg_html = f'''
        <img style="width: 200px;" src="https://github.com/Rayleigh190/Orange/assets/86937253/168590d0-1429-4088-9926-a931f4382690"/>
        <h1>📢 마니토 매칭 결과 확인</h1>
        <p>안녕하세요👋 {author}님(개설자)이 마니또 매칭 결과를 🔍확인했습니다!!</p>
        '''

        msg_body = MIMEText(msg_html, 'html')
        msg.attach(msg_body)

        try:
            s.sendmail(admin_mail, f"{manito_mail[i]}", msg.as_string())
        except Exception as e:
            print("err: ", str(e))

    s.quit()  # 세션 종료


class ManitoCreateAPIView(CreateAPIView):
    """
    마니또를 저장하고
    파트너를 생성하여 메일을 전송합니다.
    """
    queryset = Manito.objects.all()
    serializer_class = ManitoSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response({"error": "로그인이 필요합니다."}, status=401)
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = request.user.name
        manito_sender, manito_receiver, manito_mail = sendEmail(
            serializer.validated_data['name_data'],
            serializer.validated_data['mail_data'],
            serializer.validated_data['price'],
            serializer.validated_data['title'],
            serializer.validated_data['content'],
            author,
            )
        if len(manito_receiver) <= 1:
            return Response({"error: 두 개 이상의 메일을 적어주세요"}, status=400)
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

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class ManitoCheckAPIView(APIView):
    """
    마니또 만든 사람이 결과를 보면 참가자들에게 결과 열람 메일을 보냅니다.
    """

    def post(self, *args, **kargs):
        manito_id = self.kwargs['manito_id']
        try:
            manito = Manito.objects.get(id=manito_id)
            maildata = manito.mail_data
            author = manito.author
            sendCheckEmail(maildata, author)
            return Response({"message: 마니또 확인 메일 발송 완료"},
                            status=status.HTTP_200_OK)
        except:
            return Response({"error: 마니또 확인 메일 발송 실패"}, status=400)
