import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

data = np.array([
    [1, 5, 10],
    [2, 6, 12],
    [3, 8, 15]
])
plt.figure(figsize = (6,4))
sns.heatmap(data, annot = True, cmap = 'RdYlGn')
plt.title("Heatmap")
plt.show()

data2 = np.random.randint(0,100, (5,5))
plt.figure(figsize = (6,4))
sns.heatmap(data2, annot = True, cmap = 'YlGn')
plt.title("Heatmap")
plt.show()

idx = ["홍길동", "김철수", "이영희", "박민수"]
col = ["국어", "영어", "수학", "과학"]
data = np.random.randint(0,101, (4,4))
df = pd.DataFrame(data, index = idx, columns = col)
plt.figure(figsize = (6,4))
sns.heatmap(df, annot = True, cmap = 'gray', linewidths = 1, cbar_kws={"label": "점수"})
plt.title("Heatmap")
plt.show()




