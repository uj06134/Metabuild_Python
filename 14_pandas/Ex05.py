import pandas as pd
col = ("이름", "나이")
data = [("유재석", 50),("송은이", 30)]

df = pd.DataFrame(data, columns=col)
# print(df)

# 파일 쓰기
filename = "file/result.csv"
df.to_csv(filename, encoding="utf-8", mode="w", index=False) # index=False : 인덱스를 파일에 저장하지 않음 (인덱스 열이 제외됨)
                                                             # index=True  : 인덱스를 파일에 함께 저장함 (인덱스 열이 포함됨)

# 파일 읽기
df2 = pd.read_csv(filename, encoding="utf-8", index_col=0)
print(df2)

