import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family= font_name)

plt.figure(figsize=(5,4))
plt.plot([1,2,3,4],[5,6,3,8], linewidth=1.5, linestyle='--', marker='o', alpha=0.5)

plt.xlabel("x축")
plt.ylabel("y축")
plt.title("matplotlib 예제")
plt.show()