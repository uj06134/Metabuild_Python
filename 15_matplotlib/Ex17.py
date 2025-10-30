from wordcloud import WordCloud
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import re

with open('file/news.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

text = re.sub('[^ㄱ-힣\s]','',text) # 정규표현식, 바꿀문자열, 대상문자열
okt = Okt(jvmpath="C:/Program Files/Java/jdk-17/bin/server/jvm.dll")
print(okt.pos("안녕하세요. 형태소 분석기 테스트 중입니다."))

wc = WordCloud(
    width=800,
    height=600,
    background_color='white',
    font_path="c:\Windows\Fonts\malgun.ttf",
).generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()