import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

idx = ["웬디", "슬기", "조이"]
col = ["국어", "영어", "수학"]
data = [
    [40, 50, 50],
    [70, 50, 20],
    [20, 20, 20],
]
df = pd.DataFrame(data, index=idx, columns=col)
print(df)

# df.plot(kind="bar")
df.T.plot(kind="bar") # 컬럼, 인덱스 전치
# df.plot.bar(stacked=True) # 누적 막대 그래프
# df.plot.barh() # 가로 막대 그래프
plt.xticks(rotation=0) # x축 label 기울기 조정
plt.show()