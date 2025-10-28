import pandas as pd
df = pd.read_csv("file/movies.csv", encoding="utf-8")
print(df)

# 장르별 평점 평균
df2 = df.groupby("장르")["평점"].mean()
print(df2)

# 감독별 총 관객수
df3 = df.groupby("감독")["관객수(만)"].sum()
print(df3)

# 장르별 총 통계
df4 = df.groupby("장르").agg({"평점": "mean", "관객수(만)": "sum"})
print(df4)
df4.to_csv("movie_genre.csv", encoding="utf-8")

df5 = df.groupby(['감독', '장르'])[['평점', '관객수(만)']].mean()
print(df5)