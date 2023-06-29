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

        msg_html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="x-apple-disable-message-reformatting" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title></title>

    <style type="text/css">
      @media only screen and (min-width: 620px) {
        .u-row {
          width: 600px !important;
        }
        .u-row .u-col {
          vertical-align: top;
        }

        .u-row .u-col-22p01 {
          width: 132.06000000000003px !important;
        }

        .u-row .u-col-38p66 {
          width: 231.95999999999995px !important;
        }

        .u-row .u-col-39p33 {
          width: 235.98px !important;
        }

        .u-row .u-col-100 {
          width: 600px !important;
        }
      }

      @media (max-width: 620px) {
        .u-row-container {
          max-width: 100% !important;
          padding-left: 0px !important;
          padding-right: 0px !important;
        }
        .u-row .u-col {
          min-width: 320px !important;
          max-width: 100% !important;
          display: block !important;
        }
        .u-row {
          width: 100% !important;
        }
        .u-col {
          width: 100% !important;
        }
        .u-col > div {
          margin: 0 auto;
        }
      }
      body {
        margin: 0;
        padding: 0;
      }

      table,
      tr,
      td {
        vertical-align: top;
        border-collapse: collapse;
      }

      p {
        margin: 0;
      }

      .ie-container table,
      .mso-container table {
        table-layout: fixed;
      }

      * {
        line-height: inherit;
      }

      a[x-apple-data-detectors="true"] {
        color: inherit !important;
        text-decoration: none !important;
      }

      table,
      td {
        color: #000000;
      }
      #u_body a {
        color: #0000ee;
        text-decoration: underline;
      }
      @media (max-width: 480px) {
        #u_content_social_1 .v-container-padding-padding {
          padding: 30px 10px 10px !important;
        }
        #u_content_text_6 .v-container-padding-padding {
          padding: 10px 10px 20px !important;
        }
        #u_content_image_2 .v-container-padding-padding {
          padding: 20px 10px 30px !important;
        }
      }
    </style>
  </head>
        '''

        msg_html += f'''
        <body
    class="clean-body u_body"
    style="
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      background-color: #ecf0f1;
      color: #000000;
    "
  >
    <table
      id="u_body"
      style="
        border-collapse: collapse;
        table-layout: fixed;
        border-spacing: 0;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        vertical-align: top;
        min-width: 320px;
        margin: 0 auto;
        background-color: #ecf0f1;
        width: 100%;
      "
      cellpadding="0"
      cellspacing="0"
    >
      <tbody>
        <tr style="vertical-align: top">
          <td
            style="
              word-break: break-word;
              border-collapse: collapse !important;
              vertical-align: top;
            "
          >
            <div
              class="u-row-container"
              style="
                padding: 0px;
                background-image: url('images/image-8.png');
                background-repeat: no-repeat;
                background-position: center top;
                background-color: transparent;
              "
            >
              <div
                class="u-row"
                style="
                  margin: 0 auto;
                  min-width: 320px;
                  max-width: 600px;
                  overflow-wrap: break-word;
                  word-wrap: break-word;
                  word-break: break-word;
                  background-color: transparent;
                "
              >
                <div
                  style="
                    border-collapse: collapse;
                    display: table;
                    width: 100%;
                    height: 100%;
                    background-color: transparent;
                  "
                >
                  <div
                    class="u-col u-col-100"
                    style="
                      max-width: 320px;
                      min-width: 600px;
                      display: table-cell;
                      vertical-align: top;
                    "
                  >
                    <div style="height: 100%; width: 100% !important">
                      <div
                        style="
                          box-sizing: border-box;
                          height: 100%;
                          padding: 0px;
                          border-top: 0px solid transparent;
                          border-left: 0px solid transparent;
                          border-right: 0px solid transparent;
                          border-bottom: 0px solid transparent;
                        "
                      >
                        <table
                          style="font-family: 'Open Sans', sans-serif"
                          role="presentation"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="v-container-padding-padding"
                                style="
                                  overflow-wrap: break-word;
                                  word-break: break-word;
                                  padding: 0px;
                                  font-family: 'Open Sans', sans-serif;
                                "
                                align="left"
                              >
                                <table
                                  width="100%"
                                  cellpadding="0"
                                  cellspacing="0"
                                  border="0"
                                >
                                  <tr>
                                    <td
                                      style="
                                        padding-right: 0px;
                                        padding-left: 0px;
                                      "
                                      align="center"
                                    >
                                      <img
                                        align="center"
                                        border="0"
                                        src="https://github.com/Rayleigh190/Orange/assets/86937253/2fd084b9-c9ed-4900-9c0f-77797b791d00"
                                        alt="image"
                                        title="image"
                                        style="
                                          outline: none;
                                          text-decoration: none;
                                          -ms-interpolation-mode: bicubic;
                                          clear: both;
                                          display: inline-block !important;
                                          border: none;
                                          height: auto;
                                          float: none;
                                          width: 100%;
                                          max-width: 600px;
                                        "
                                        width="600"
                                      />
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <table
                          style="font-family: 'Open Sans', sans-serif"
                          role="presentation"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="v-container-padding-padding"
                                style="
                                  overflow-wrap: break-word;
                                  word-break: break-word;
                                  padding: 10px 10px 5px;
                                  font-family: 'Open Sans', sans-serif;
                                "
                                align="left"
                              >
                                <div
                                  style="
                                    font-size: 17px;
                                    color: #000000;
                                    line-height: 140%;
                                    text-align: center;
                                    word-wrap: break-word;
                                  "
                                >
                                  <p style="line-height: 140%">
                                    Follow The Party Live:
                                  </p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <table
                          style="font-family: 'Open Sans', sans-serif"
                          role="presentation"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="v-container-padding-padding"
                                style="
                                  overflow-wrap: break-word;
                                  word-break: break-word;
                                  padding: 0px 10px;
                                  font-family: 'Open Sans', sans-serif;
                                "
                                align="left"
                              >
                                <h1
                                  style="
                                    margin: 0px;
                                    color: #000000;
                                    line-height: 140%;
                                    text-align: center;
                                    word-wrap: break-word;
                                    font-family: Great Vibes;
                                    font-size: 35px;
                                    font-weight: 400;
                                  "
                                >
                                  <strong
                                    >{title}<br />
                                    💌 초대장 💌</strong
                                  >
                                </h1>
                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <table
                          style="font-family: 'Open Sans', sans-serif"
                          role="presentation"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="v-container-padding-padding"
                                style="
                                  overflow-wrap: break-word;
                                  word-break: break-word;
                                  padding: 5px 50px 30px;
                                  font-family: 'Open Sans', sans-serif;
                                "
                                align="left"
                              >
                                <div
                                  style="
                                    font-size: 14px;
                                    color: #000000;
                                    line-height: 140%;
                                    text-align: center;
                                    word-wrap: break-word;
                                  "
                                >
                                  <p style="line-height: 140%">
                                    <span
                                      data-metadata="&lt;!--(figmeta)eyJmaWxlS2V5IjoiMzJNeHRiVWVOVVdibnNaR2lHMTVyMCIsInBhc3RlSUQiOjE1NDI3MjgwNywiZGF0YVR5cGUiOiJzY2VuZSJ9Cg==(/figmeta)--&gt;"
                                      style="line-height: 19.6px"
                                    ></span
                                    >{author}님이 당신을 초대했습니다!<br />
                                    안녕하세요 {manito_sender[i]}님~<br />저희는
                                    TEAM 모마 입니다👋<br />저희는 여러분의
                                    마니또 매칭을 도와드립니다 🎉
                                  </p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div
              class="u-row-container"
              style="padding: 0px; background-color: transparent"
            >
              <div
                class="u-row"
                style="
                  margin: 0 auto;
                  min-width: 320px;
                  max-width: 600px;
                  overflow-wrap: break-word;
                  word-wrap: break-word;
                  word-break: break-word;
                  background-color: transparent;
                "
              >
                <div
                  style="
                    border-collapse: collapse;
                    display: table;
                    width: 100%;
                    height: 100%;
                    background-image: url('images/image-7.png');
                    background-repeat: no-repeat;
                    background-position: center top;
                    background-color: transparent;
                  "
                >
                  <div
                    class="u-col u-col-38p66"
                    style="
                      max-width: 320px;
                      min-width: 231.96px;
                      display: table-cell;
                      vertical-align: top;
                    "
                  >
                    <div
                      style="
                        height: 100%;
                        width: 100% !important;
                        border-radius: 0px;
                        -webkit-border-radius: 0px;
                        -moz-border-radius: 0px;
                      "
                    >
                      <div
                        style="
                          box-sizing: border-box;
                          height: 100%;
                          padding: 0px;
                          border-top: 1px solid #ccc;
                          border-left: 0px solid transparent;
                          border-right: 1px solid #ccc;
                          border-bottom: 1px solid #ccc;
                          border-radius: 0px;
                          -webkit-border-radius: 0px;
                          -moz-border-radius: 0px;
                        "
                      >
                        <table
                          style="font-family: 'Open Sans', sans-serif"
                          role="presentation"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="v-container-padding-padding"
                                style="
                                  overflow-wrap: break-word;
                                  word-break: break-word;
                                  padding: 20px;
                                  font-family: 'Open Sans', sans-serif;
                                "
                                align="left"
                              >
                                <div
                                  style="
                                    font-size: 14px;
                                    color: #000000;
                                    line-height: 150%;
                                    text-align: center;
                                    word-wrap: break-word;
                                  "
                                >
                                  <p style="font-size: 14px; line-height: 150%">
                                    <span
                                      style="font-size: 18px; line-height: 27px"
                                      ><span
                                        style="
                                          font-family: Montserrat, sans-serif;
                                          line-height: 27px;
                                          font-size: 22px;
                                        "
                                        >🧚‍♀️ 당신의 마니또는?
                                      </span></span
                                    >
                                  </p>
                                  <p style="font-size: 14px; line-height: 150%">
                                    <span
                                      style="font-size: 18px; line-height: 27px"
                                      ><span
                                        style="
                                          font-family: Montserrat, sans-serif;
                                          line-height: 27px;
                                          font-size: 22px;
                                        "
                                        >{shuffle_manito[i]}</span
                                      ></span
                                    >
                                  </p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                  <div
                    class="u-col u-col-39p33"
                    style="
                      max-width: 320px;
                      min-width: 235.98px;
                      display: table-cell;
                      vertical-align: top;
                    "
                  >
                    <div
                      style="
                        height: 100%;
                        width: 100% !important;
                        border-radius: 0px;
                        -webkit-border-radius: 0px;
                        -moz-border-radius: 0px;
                      "
                    >
                      <div
                        style="
                          box-sizing: border-box;
                          height: 100%;
                          padding: 0px;
                          border-top: 1px solid #ccc;
                          border-left: 1px solid #ccc;
                          border-right: 0px solid transparent;
                          border-bottom: 1px solid #ccc;
                          border-radius: 0px;
                          -webkit-border-radius: 0px;
                          -moz-border-radius: 0px;
                        "
                      >
                        <table
                          style="font-family: 'Open Sans', sans-serif"
                          role="presentation"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="v-container-padding-padding"
                                style="
                                  overflow-wrap: break-word;
                                  word-break: break-word;
                                  padding: 20px;
                                  font-family: 'Open Sans', sans-serif;
                                "
                                align="left"
                              >
                                <div
                                  style="
                                    font-size: 14px;
                                    color: #000000;
                                    line-height: 150%;
                                    text-align: center;
                                    word-wrap: break-word;
                                  "
                                >
                                  <p style="font-size: 14px; line-height: 150%">
                                    <span
                                      style="font-size: 18px; line-height: 27px"
                                      ><span
                                        style="
                                          font-family: Montserrat, sans-serif;
                                          line-height: 27px;
                                          font-size: 22px;
                                        "
                                        >💰선물의 예산은?
                                      </span></span
                                    >
                                  </p>
                                  <p style="font-size: 14px; line-height: 150%">
                                    <span
                                      style="font-size: 18px; line-height: 27px"
                                      ><span
                                        style="
                                          font-family: Montserrat, sans-serif;
                                          line-height: 27px;
                                          font-size: 22px;
                                        "
                                        >{price}원</span
                                      ></span
                                    >
                                  </p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div
              class="u-row-container"
              style="
                padding: 0px;
                background-image: url('images/image-7.png');
                background-repeat: no-repeat;
                background-position: center bottom;
                background-color: transparent;
              "
            >
              <div
                class="u-row"
                style="
                  margin: 0 auto;
                  min-width: 320px;
                  max-width: 600px;
                  overflow-wrap: break-word;
                  word-wrap: break-word;
                  word-break: break-word;
                  background-color: transparent;
                "
              >
                <div
                  style="
                    border-collapse: collapse;
                    display: table;
                    width: 100%;
                    height: 100%;
                    background-color: transparent;
                  "
                >
                  <div
                    class="u-col u-col-100"
                    style="
                      max-width: 320px;
                      min-width: 600px;
                      display: table-cell;
                      vertical-align: top;
                    "
                  >
                    <div
                      style="
                        height: 100%;
                        width: 100% !important;
                        border-radius: 0px;
                        -webkit-border-radius: 0px;
                        -moz-border-radius: 0px;
                      "
                    >
                      <div
                        style="
                          box-sizing: border-box;
                          height: 100%;
                          padding: 0px;
                          border-top: 0px solid transparent;
                          border-left: 0px solid transparent;
                          border-right: 0px solid transparent;
                          border-bottom: 0px solid transparent;
                          border-radius: 0px;
                          -webkit-border-radius: 0px;
                          -moz-border-radius: 0px;
                        "
                      >
                        <table
                          style="font-family: 'Open Sans', sans-serif"
                          role="presentation"
                          cellpadding="0"
                          cellspacing="0"
                          width="100%"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                class="v-container-padding-padding"
                                style="
                                  overflow-wrap: break-word;
                                  word-break: break-word;
                                  padding: 45px 10px 60px;
                                  font-family: 'Open Sans', sans-serif;
                                "
                                align="left"
                              >
                                <div align="center">
                                  <a
                                    href="https://modumanito.site/"
                                    target="_blank"
                                    class="v-button"
                                    style="
                                      box-sizing: border-box;
                                      display: inline-block;
                                      font-family: 'Open Sans', sans-serif;
                                      text-decoration: none;
                                      -webkit-text-size-adjust: none;
                                      text-align: center;
                                      color: #ffffff;
                                      background-color: #ba372a;
                                      border-radius: 4px;
                                      -webkit-border-radius: 4px;
                                      -moz-border-radius: 4px;
                                      width: 44%;
                                      max-width: 100%;
                                      overflow-wrap: break-word;
                                      word-break: break-word;
                                      word-wrap: break-word;
                                      mso-border-alt: none;
                                      font-size: 22px;
                                    "
                                  >
                                    <span
                                      style="
                                        display: block;
                                        padding: 10px 20px;
                                        line-height: 120%;
                                      "
                                      ><span style="line-height: 16.8px"
                                        >나도 마니또 만들러 가기</span
                                      ></span
                                    >
                                  </a>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="u-row-container"
              style="padding: 0px; background-color: transparent"
            >
              <div
                class="u-row"
                style="
                  margin: 0 auto;
                  min-width: 320px;
                  max-width: 600px;
                  overflow-wrap: break-word;
                  word-wrap: break-word;
                  word-break: break-word;
                  background-color: transparent;
                "
              >
                <div
                  style="
                    border-collapse: collapse;
                    display: table;
                    width: 100%;
                    height: 100%;
                    background-color: transparent;
                  "
                >
                  <div
                    class="u-col u-col-100"
                    style="
                      max-width: 320px;
                      min-width: 600px;
                      display: table-cell;
                      vertical-align: top;
                    "
                  ></div>
                </div>
              </div>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
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
        <img style="width: 200px;" src="https://github.com/Rayleigh190/Orange/assets/86937253/43b84b90-49e7-489b-81d8-e13f986c7e18"/>
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
