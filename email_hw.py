from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

## 스크래핑
driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "썸네일"])

articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

for article in articles:
    a_tag = article.select_one('div.news_wrap.api_ani_send > div > a')
    title = a_tag.text
    url = a_tag['href']

    # comp = article.select_one('#text')
    # comp = article.select_one('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press > span').text.split(' ')[0].replace('언론사','')

    preview = article.select_one('div.news_wrap.api_ani_send > a > img')['src']
    print(preview)
    ws1.append([title, url, preview])

driver.quit()
wb.save(filename='articles.xlsx')

# 메일 보내기
# 보내는 사람 정보
me = "narin1101@gmail.com"
my_password = ""

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
you = "snya0055@naver.com"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "메리추석"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "복 많이 받을거야"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 파일 첨부하기
part = MIMEBase('application', "octet-stream")
with open("articles.xlsx", 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename="merrychuseok.xlsx")
msg.attach(part)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()