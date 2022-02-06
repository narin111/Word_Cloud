import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 드라이버로 페이지 띄워주세요
# 띄우는 시간이 걸리니까 쉬어!
driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

# 페이지에서 받아온 것을 req에 저장
req = driver.page_source
# bs4에 넣고
soup = BeautifulSoup(req, 'html.parser')
# 원하는 부분만 가져오겠다. - 썸네일 태그 값들, div에서 규칙찾기
thumbnails = soup.select("#imgList > div > a > img")

i=1
# 썸네일 이미지 링크 값을 반복문으로 가져온다.
# hello.py와 같은 깊이의 imgs 폴더에 저장한다. - dload 사용
for thumbnail in thumbnails:
    src = thumbnail["src"]
    dload.save(src, f'imgs/{i}.jpg') 
    i+=1

# 끝나면 닫아주기
driver.quit()