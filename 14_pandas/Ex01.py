import pandas as pd

# 1차원 자료구조
# 인덱스(index) + 값(value)
s1 = pd.Series([10,20,30,40])
print(f"s1:\n{s1}")
print(type(s1))
print(s1.index)
print(s1.values)
print("-------------------")

s2 = pd.Series([10,20,30,40], index=['a','b','c','d'])
print(f"s2:\n{s2}")
print(s2['a'])
print(type(s2))
print(s2.index)
print(s2.values)
# 값 수정
s2['d'] = 35
print(f"s2:\n{s2}")
print(s2[['a','b']])
print(s2[(s2.values >= 20) & (s2.values <= 30)])
print(s2.index == "a")
print(s2 * 2)
print('a' in s2.index)
print(10 in s2.values)
print("-------------------")

d = {"서울":2000, "부산":3000, "울산": 7000, "광주": 5000}
s3 = pd.Series(d) # 딕셔너리를 Series로 변환 (key=인덱스, value=값)
print(f"s2:\n{s2}")
print("-------------------")

city = ["부산", "울산", "인천", "서울"]
s4 = pd.Series(d, index=city)  # 지정한 인덱스 순서로 Series 생성 (없는 값은 NaN)
print(f"s3:\n{s4}")


# NaN(결측값) 여부 확인 (True/False)
print(pd.isna(s4))
print(pd.isnull(s4))
# NaN이 아닌 값 확인 (True/False)
print(pd.notna(s4))
print([pd.notnull(s4)])
print("-------------------")

s5 = pd.Series([10,20,30,40], index=['a','b','c','d'])
s5_drop = s5.drop(['a','b'])
print(f"s5_drop:\n{s5_drop}")
print(f"s5:\n{s5}")

print(s5[2:4])
print(s5.iloc[[1,3]])
print(s5[3:1:-1])

sort_index = s5.sort_index()
print(f"sort_index:\n{sort_index}")
sort_values = s5.sort_values(ascending=False)
print(f"sort_values:\n{sort_values}")
