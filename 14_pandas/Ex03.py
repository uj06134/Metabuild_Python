import pandas as pd
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr[1][2])
print(arr[1,2])
print("-----------------")

# DataFrame: 2차원(행/열) 자료구조
df1 = pd.DataFrame(arr)
print(df1)
print(type(df1))
print(df1[2][1])

s1 = pd.Series([10,20,30,40])
s2 = pd.Series(['A','B','C','D'])

df2 = pd.DataFrame([s1, s2])
print(df2)

d = {'a':[1,3],'b':[4,7],'c':[5,2]}
df3 = pd.DataFrame(d)
print(df3)

df4 = pd.DataFrame(data=[[4,5,6,7],[1,2,3,4]],
                   index=['man','woman'],
                   columns=['A','B','C','D'])

print(df4.iloc[1,2])

df5 = pd.DataFrame(data=[["윤아","영업",5000,2],
                         ["민호","개발",6000,5],
                         ["혜수","개발",5500,3],
                         ["찬열","영업",5800,4],
                         ["소영","인사",4800,1]],
                   columns=['이름','부서','급여','근속연수'])
print(df5)

d = {"이름":["윤아","민호","혜수","찬열","소영"],
     "부서":["영업","개발","개발","영업","인사"],
     "급여":[5000,6000,5500,5800,4800],
     "근속연수":[2,5,3,2,1]}
df6 = pd.DataFrame(d)
print(df6)

# 연봉 컬럼 추가
df6["연봉"] = df6["급여"] * 12
print(df6)

# 이름, 연봉 컬러만 출력
print(df6[["이름", "연봉"]])

# 인덱스 변경
df6.index = ["one","two","three","four","five"]
print(df6)

# 인덱스가 three인 value 출력
print(df6[df6.index == "three"])
print(df6.loc["three"])

# 상여금 컬럼 추가
# df6["상여금"] = [300, 500, 400, 450, 200]
bonus = pd.Series([300, 500, 400, 450, 200], index=["one","two","three","four","five"])
df6["상여금"] = bonus

print(df6)

# 총연봉
df6["총연봉"] = df6["연봉"] + df6["상여금"]
print(df6)

# 상여금 비율 추가
# 상여금/급여
df6["상여금 비율"] = round(df6["상여금"] / df6["급여"],2)
print(df6)

# 컬럼과 인덱스 전치
df6_t = df6.transpose()
print(df6_t)
df6_t = df6_t.T
print(df6_t)

print(df5)

df = pd.DataFrame(data=[["윤아","영업",5000,2],
                         ["민호","개발",6000,5],
                         ["혜수","개발",5500,3],
                         ["찬열","영업",5800,4],
                         ["소영","인사",4800,1]],
                   columns=['이름','부서','급여','근속연수'])
print(df)
# df.index = ["one","two","three","four","five"]

# 행 삭제 (0, 4행 제거)
df_drop = df.drop([0, 4])
print(df_drop)

# 컬럼 삭제 (급여, 근속연수)
df_drop = df.drop(["급여","근속연수"], axis=1)
print(df_drop)

# 특정 행과 컬럼 동시에 삭제 (1,3행 + 급여 컬럼)
df_drop = df.drop(index=[1, 3], columns=['급여'])
print(df_drop)

# 인덱스 위치 변경
df_reindex = df.reindex([4,2,0,1,3])
print(df_reindex)

# 컬럼 위치 변경
df_reindex = df.reindex(columns=["이름", "근속연수", "급여", "부서"])
print(df_reindex)

# 부서가 '인사'인 컬럼 삭제
df_drop = df.drop(df[df["부서"]=="인사"].index)
# print(df_drop)

# 부서가 '개발'인 컬럼 삭제
df_drop2 = df[df["부서"] != "개발"]
# print(df_drop2)

# 급여가 5500이상인 데이터
df_filter = df[df["급여"]>=5500]
print(df_filter)

# 근속연수 기준 내림차순 정렬
df_sort = df.sort_values(by="근속연수", ascending=False).reset_index(drop=True)
print(df_sort)

# 부서 기준 오름차순, 급여 기준 내림차순 정렬
df_sort = df.sort_values(by=["부서","급여"], ascending=[True,False]).reset_index(drop=True)
print(df_sort)