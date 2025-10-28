import pandas as pd

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드',
            'TCS하이패스구분코드', '1종교통량', '2종교통량',
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량']

df = pd.read_csv("file/capital_area.csv", sep="|", header=None, names=mycolumn, index_col=False)
# df = pd.read_table("capital_area.csv", sep="|", header=None)
print(df.head())

# 영업소코드
print(df["영업소코드"])

# 컬럼 여러개
print(df[["영업소코드", "1종교통량", "총교통량"]])

# 영업소 코드 별로 그룹
mygroup = df.groupby("영업소코드")
# print(mygroup)

# 영업소코드별 총교통량 합계
df2 = mygroup["총교통량"].sum()
# df2 = df.groupby("영업소코드")["총교통량"].sum()  # 한 줄로도 가능
print(df2)

# 영업소코드별 1종, 2종, 총교통량 합계
df3 = df.groupby("영업소코드")[["1종교통량", "2종교통량", "총교통량"]].sum()
print(df3)

# 영업소코드가 190이고, 입출구구분코드가 1인 데이터 추출 (조건 필터링)
df4 = df[(df["영업소코드"] == 190) & (df["입출구구분코드"] == 1)]
print(df4)

# 1종교통량의 전체 최댓값
max1 = df["1종교통량"].max()
print(max1)

# 1종교통량의 전체 최솟값
min1 = df["1종교통량"].min()
print(min1)

# 영업소코드별 1종교통량의 최댓값
df5 = df.groupby("영업소코드")["1종교통량"].max()
print(df5)

# 영업소코드별 1종교통량, 2종교통량의 최댓값과 최솟값을 동시에 계산
df6 = df.groupby("영업소코드")[["1종교통량", "2종교통량"]].agg(["max", "min"])
print(df6)

# 집계일자별 총교통량의 평균
df7 = df.groupby("집계일자")["총교통량"].mean()
print(df7)

# 집계일자, 집계시별 총교통량 합계
df8 = df.groupby(["집계일자", "집계시"])["총교통량"].sum()
print(df8)

# 집계시가 7시~9시인 데이터만 필터링 후, 집계일자·집계시별 총교통량 합계 계산
df_filter = df[(df["집계시"] >= 7) & (df["집계시"] <= 9)]
df9 = df_filter.groupby(['집계일자',"집계시"])['총교통량'].sum().reset_index()
print(df9)

# 집계일자가 2023년 2월 1일인 데이터만 추출
df10 = df9[df9["집계일자"] == 20230201].sum()
print(df10)

df11 = df.groupby("집계일자")["총교통량"].sum().reset_index()
df11 = df11[df11["총교통량"] > 800000]
print(df11)