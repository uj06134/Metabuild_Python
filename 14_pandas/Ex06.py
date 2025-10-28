import pandas as pd

df = pd.read_csv("file/read.csv", encoding="utf-8", index_col=0, header=0)
print(df)

# 결측치
print(df.isnull())
# print(df.isna())
# print(pd.isnull(df))

print(df.notnull())
print(df.notna())

# 결측치 제거
print(df.dropna(subset=["kor"])) # subset=["col"]: 특정 컬럼 선택

df.fillna({"kor": 22, "eng": 33}, inplace=True)
print(df)

