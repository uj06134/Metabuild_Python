import pandas as pd

df1 = pd.DataFrame({'고객번호':[1001,1002,1003,1004,1005],
                    '이름':['윤아','수영','서현','효연','써니']
                    },columns=['고객번호','이름'])

print('df1:\n',df1)
print()
df2 = pd.DataFrame({
                '고객번호': [1001, 1007, 1003, 1004, 1002, 1001],
                '금액': [10000, 20000, 15000, 5000, 100000, 30000]
                }, columns=['고객번호', '금액'])
print('df2:\n',df2)
print()

# merge() : 두 DataFrame을 특정 컬럼(기본은 공통 컬럼명 기준)으로 병합
print(pd.merge(df1, df2, how='inner')) # 기본값 (inner 생략 가능)
print(pd.merge(df1, df2, how='left'))
print(pd.merge(df1, df2, how='right'))
print(pd.merge(df1, df2, how='outer'))

print("-----------------------")
df1 = pd.DataFrame({
                    '고객명': ['춘향', '춘향', '몽룡'],
                    '날짜': ['2021-01-01', '2021-01-02', '2021-01-03'],
                    '데이터': ['100','200','300']})

df2 = pd.DataFrame({
                    '고객명': ['춘향', '몽룡','향단'],
                    '데이터': ['여자', '남자','여자'],
                    '주소':['경기','서울','부산']})

print('df1:\n',df1)
print('df2:\n',df2)

# '고객명' 컬럼을 기준으로 병합
# 양쪽에 같은 이름의 컬럼('데이터')이 존재하므로 suffixes로 이름 구분
# suffixes=("1", "2") → df1의 '데이터' → '데이터1', df2의 '데이터' → '데이터2'
print(pd.merge(df1, df2, on="고객명", suffixes=("1", "2")))

df1 = pd.DataFrame({
                    '이름': ['춘향', '춘향', '몽룡'],
                    '날짜': ['2021-01-01', '2021-01-02', '2021-01-03'],
                    '데이터': ['100','200','300']})

df2 = pd.DataFrame({
                    '성명': ['춘향', '몽룡','향단'],
                    '데이터': ['여자', '남자','여자'],
                    '주소':['경기','서울','부산']})
print('df1:\n',df1)
print('df2:\n',df2)

# left_on / right_on :
# 병합 기준 컬럼명이 서로 다를 때 각각 지정
print(pd.merge(df1, df2, left_on="이름", right_on="성명", suffixes=("1", "2")))
m = pd.merge(df1, df2, left_on="이름", right_on="성명")

m.drop(columns=["성명","데이터_x"], inplace=True)
# m = m.reindex(columns=['이름', '날짜', '데이터_y', '주소'])
print(m)
