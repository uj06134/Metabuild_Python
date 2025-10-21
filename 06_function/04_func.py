# lambda 매개변수1, 매개변수2, ... : 반환값
a = lambda x : x ** 2
print(a(2))

b = lambda x, y : x+y
print(b(10,20))

L = [1,2,3,4,5]
# map(함수, 반복 가능한 객체)
# → L의 각 요소에 lambda x:x**2 함수를 적용한 결과를 반환 (map 객체 형태)
result = list(map(lambda x : x ** 2, L))
print(result)

fruit = ['apple', 'banana', 'cherry', 'kiwi']
result2 = list(map(lambda x : len(x), fruit))
print(result2)

a = [1,2,3]
b = [10,20,30]

result3 = list(map(lambda x,y : x+y , a, b))
print(result3)

L = [13,16,11,15,14]
result4 = list(map(lambda x : "짝수" if x % 2 == 0 else "홀수", L))
print(result4)

fruit = ['apple', 'banana', 'cherry', 'kiwi']
result5 = list(map(lambda x : (x.upper(),len(x)), fruit))
print(result5)

students = [
    ["kim", 90, 10],
    ["park", 80, 30],
    ["choi", 70, 50],
    ["jung", 60, 70],
    ["hong", 50, 90],
]

students.sort(key=lambda x : (-x[-1], x[2]))
print(students)

L = [13,16,11,15,14]
result6 = list(filter(lambda x : x % 2 == 0, L)) # 짝수만 가져오기
print(result6)

fruit = ['apple', 'banana', 'cherry', 'kiwi']
result7 = list(filter(lambda x : len(x) >= 6, fruit))
print(result7)

print("------------Ex12--------------")
students = [
    ["kim", 90, 90],
    ["park", 85, 71],
    ["choi", 90, 75],
    ["jung", 45, 82],
    ["hong", 87, 87]
]

result8 = list(filter(lambda x : x[1]>=80, students))
print("국 80점 이상 :", result8)

result9 = list(filter(lambda x : (x[1]>=87 and x[2]>=87), students))
print("국,영 87이상 :",result9)

# 튜플(kim,평균), (jung,평균)  튜플로 묶꼬 리스트로 만들기
result10 = list(map(lambda x: (x[0], (x[1]+x[2])/2), students))
print(result10)

# result에서 평균이 80이상 걸러내기
result11 = list(filter(lambda x : x[1] >= 80, result10))
print(result11)

# dict에서 평균이 70이상 걸러내기
score = {
    '윤아': {'국어':65, '수학':92, '영어':74},
    '정국': {'국어':15, '수학':12, '영어':13},
    '태연': {'국어':41, '수학':25, '영어':78},
    '보검': {'국어':75, '수학':83, '영어':75}
}

dict = {}
for name in score.keys():
    total = sum(score[name].values())
    sub_count = len(score[name])
    avg = round(total / sub_count, 2)
    dict[name] = avg

result12 = list(filter(lambda x : x[1] >= 70, dict.items()))
print(result12)