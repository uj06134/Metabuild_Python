import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

slices = [1, 2, 3, 4]
hobbies = ["공부", "게임", "영화 감상", "운동"]
colors = ["r", "g", "b", "y"]
plt.title("취미 비율")
plt.pie(slices, labels=hobbies, colors=colors, startangle=90, explode=(0.1,0,0,0), autopct='%1.1f%%')
plt.legend(loc=0)
plt.show()