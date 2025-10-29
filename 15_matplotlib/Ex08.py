import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

cases = ["케이스1", "케이스2", "케이스3"]
xlabels = ["대식구", "출퇴근시간", "깔끔한집"]
mylabels = ["방의 개수", "위치", "건축년도"]
data = [(100,60,30),(30,100,60),(60,30,100)]

plt.figure(figsize=(15, 5))
for i in range(len(cases)):
    plt.subplot(1, len(cases), i + 1)
    plt.pie(data[i], labels=mylabels, startangle=90, autopct='%1.1f%%')
    plt.title(f"주요 요소 : {mylabels[i]}", fontweight="bold")
    plt.xlabel(xlabels[i])
plt.show()