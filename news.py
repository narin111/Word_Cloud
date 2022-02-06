from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook


driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크"])

# 선택한 elements의 태그까지 다 나옴
# print(articles)

for article in articles:
    title = article.select_one(' div.news_wrap.api_ani_send > div > a')
    url = article.select_one('div.news_wrap.api_ani_send > div > a')['href']
    # comp = article.select_one('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press > span')
    print(title.text)
    print(url)
    # print(comp.text)
    ws1.append([title, url])

driver.quit()
wb.save(filename = 'articles.xlsx')