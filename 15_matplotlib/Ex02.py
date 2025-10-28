import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family= font_name)

x1 = [1,2,3,4]
y1 = [3,7,6,4]
x2 = [1,2,3,4]
y2 = [4,6,8,5]

ymax = max(max(y1), max(y2))
print(ymax)

ymin = min(min(y1), min(y2))
print(ymin)

plt.plot(x1, y1, label="first line", color='r', linestyle='dotted', marker='s')
plt.plot(x2, y2, label="second line", color='b', linestyle='dotted')
plt.ylim(ymin-1, ymax+1)
plt.xlabel("x축")
plt.ylabel("y축")
plt.title("matplotlib 예제")
plt.legend() # 범례
plt.annotate("annotate", xy=(1.5,5), xytext=(2,4), arrowprops={"color":"g"})

# 파일 저장
filename = "file/brokenLines.png"
plt.savefig(filename)
plt.show()
