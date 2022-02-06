from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("sister.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        if '] [' in line:
            # 카톡에서 쓴 이모티콘은 텍스트파일에서 이모티콘으로 표시된다.
            # 텍스트로 쓴 이모티콘과 진짜 이모티콘은 \n로 구별한다.
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '').replace('사진\n', '').replace(
                '이모티콘\n', '').replace('삭제된 메시지입니다', '')
            print(text)

# wc = WordCloud(font_path='C:/WINDOWS/Fonts/NanumGothic.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result2.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/WINDOWS/Fonts/NanumGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_sister.png")

