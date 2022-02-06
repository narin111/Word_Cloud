import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 받는 사람들
emails = ['snya0055@naver.com', 'siwon27@naver.com']


# 보내는 사람 정보
me = "narin1101@gmail.com"
my_password = "99rnrmffls!"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

for you in emails:
    # 받는 사람 정보
    # you = "받는사람@아무_도메인"

    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "안뇽"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "안뇽"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # # 첨부파일
    # part = MIMEBase('application', "octet-stream")
    # with open("articles.xlsx", 'rb') as file:
    #     part.set_payload(file.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    # msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())

s.quit()