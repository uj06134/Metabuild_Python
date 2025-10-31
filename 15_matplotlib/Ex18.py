from collections import Counter
from wordcloud import WordCloud
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import re

with open("file/review1.txt", encoding="utf-8") as f:
    text1 = f.read()

with open("file/review2.txt", encoding="utf-8") as f:
    text2 = f.read()


text = text1 + text2
# print(text)

text = re.sub('[^가-힣\s]','',text)
okt = Okt()
nouns = okt.nouns(text)
words = []
delete_word = ["위해", "대신", "어쩌면", "통해", "오히려"]
for noun in nouns:
    if noun not in delete_word and len(noun)>=2:
        words.append(noun)
# print(words)

count = Counter(words)
filtered = {word:freq for word,freq in count.items() if freq >= 3}
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