import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

x1 = [1,2,3,4]
y1 = [3,7,6,4]
x2 = [1,2,3,4]
y2 = [4,6,8,5]

y_max = max(max(y1), max(y2))
y_min = min(min(y1), min(y2))

plt.subplot(2,1,1)
plt.plot(x1, y1, 'yo-')
plt.xlabel('x축')
plt.ylabel('y축')
plt.ylim(y_min-1,y_max+1)
plt.title('그래프 예제')

plt.subplot(2,1,2)
plt.plot(x2, y2, 'r.--')
plt.xlabel('x축')
plt.ylabel('y축')
plt.ylim(y_min-1,y_max+1)
plt.show()

