from collections import Counter
from wordcloud import WordCloud
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import re

with open('file/news.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    # print(text)

text = re.sub('[^가-힣\s]','',text) # 정규표현식, 바꿀문자열, 대상문자열
okt = Okt()
nouns = okt.nouns(text)
# print(nouns)
delete_word = ["한지영", "등", "이민영", "이", "그", "저"]
words = [word for word in nouns if word not in delete_word and len(word)>=2]
# print(words)
count = Counter(words)


for word,freq in count.most_common(20):
    print(f"{word}: {freq}")

filtered = {word:freq for word,freq in count.items() if freq >= 4}
print(filtered)

wc = WordCloud(
    width=800,
    height=600,
    background_color='white',
    font_path="c:\Windows\Fonts\malgun.ttf",
    colormap="viridis",
    max_words=100,
    prefer_horizontal=0.9
).generate_from_frequencies(filtered)

plt.imshow(wc)
plt.axis("off")
plt.show()