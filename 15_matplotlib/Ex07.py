import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드',
            'TCS하이패스구분코드', '1종교통량', '2종교통량',
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량']

df = pd.read_csv("file/capital_area.csv", sep="|", header=None, names=mycolumn, index_col=False)
df2 = df.groupby("영업소코드")[["2종교통량","3종교통량","4종교통량","5종교통량","6종교통량"]].mean()
print(df2)
df2.plot(kind="bar")
plt.title("영업소 코드별 평균 교통량")
plt.xticks(rotation=0)
plt.show()