import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from bs4 import BeautifulSoup
import urllib.request
font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

# https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4

url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4"
soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url)).read(), "html.parser")
movie_list = []
grade_list = []

name = soup.find_all("strong", {"class": "name"})
for item in name:
    movie_list.append(item.text)

movie_list = movie_list[30:]
print(movie_list[:5])

grade = soup.find_all("span", {"class": "sub_text"})
for g in grade:
    if not "명" in g.text:
        grade_list.append(float(g.text))
print(grade_list[:5])

top5_titles = movie_list[:5]
top5_grades = grade_list[:5]

plt.figure(figsize=(15, 10))
plt.bar(movie_list[:5], grade_list[:5], color="b", alpha=0.6)
plt.ylim(min(top5_grades) - 0.05, max(top5_grades) + 0.05)
plt.title('평점 상위 5개 영화')
plt.xlabel('영화명')
plt.ylabel('평점')
plt.show()
