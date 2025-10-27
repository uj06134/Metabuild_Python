from math import trunc

import numpy as np

count = 5
su = 2

# np.repeat(값, 반복횟수): 특정 값을 원하는 횟수만큼 반복하여 배열 생성
result = np.repeat(su, count)
print(result)

arr1 = np.array([1,2])
arr2 = np.array([3,4])
print('arr1:', arr1)
print('arr2:', arr2)

# np.concatenate((arr1, arr2)): 여러 배열을 하나로 이어붙이는 함수
result = np.concatenate((arr1, arr2))
print(result)

# np.hstack(): horizontal stack (가로 방향 결합)
hs = np.hstack((arr1, arr2))
print("hs:\n",hs)

# np.vstack(): vertical stack (세로 방향  결합)
vs = np.vstack((arr1, arr2))
print("vs:\n",vs)
print("---------------")
arr = np.array([1.57, 2.48, 3.93, 4.33, 2.21])
print("arr:", arr)
# np.ceil(x): 올림 (Ceiling)
result = np.ceil(arr)
print("ceil:", result)

# np.floor(x): 내림 (Floor)
result = np.floor(arr)
print("floor:", result)

# np.trunc(x): 버림 (Truncate)
result = np.trunc(arr)
print("trunc:", result)

# np.round(x, n): 소수점 n자리에서 반올림 (Round)
result = np.round(arr, 1)
print("round:", result)

# np.sqrt(x): 제곱근(Square Root)
sqrt = np.sqrt(arr)
print("sqrt:", sqrt)

# np.square(x) : 제곱(Square)
square = np.square(arr)
print("square:", square)

arr = np.sum(arr), np.average(arr), np.mean(arr), np.max(arr), np.min(arr)
print("arr:", arr)

arr1 = np.array([1.57, 2.48, 3.93, 4.33, 2.21])
arr2 = np.array([1.58, 2.49, 3.94, 4.34, 2.22])
arr3 = np.array([23.57, 2.48, 3.93, 4.33, 2.21])
print(np.max(arr1))
# np.maximum(arr1, arr2): 두 배열의 각 위치별로 큰 값을 선택해 반환
print(np.maximum(arr1, arr2))
print(np.equal(arr1, arr3))

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

print("arr1:\n", arr1)
print("arr2:\n", arr2)

print("전체 합계:", np.sum(arr1))                     # 배열 전체 합
print("열(axis=0) 기준 합계:", np.sum(arr1, axis=0))  # 각 열의 합
print("행(axis=1) 기준 합계:", np.sum(arr1, axis=1))  # 각 행의 합

# np.random.seed(0)
random_value = np.random.random()
print("random_value:", random_value)
print(int(random_value * 10)+5)
print(int(random_value * 45)+1)

import random
print(random.random())
print(random.randrange(1,46, 1))
print(np.random.randint(1, 46, 5))
# 다차원 난수 배열 생성
print(np.random.randint(1, 46, (2,2)))

# 중복 O
list1 = []
for i in range(10):
    num = random.randrange(1,11)
    list1.append(num)
print(list1)

# 중복 X
list2 = random.sample(range(1,11), 10)
print(list2)