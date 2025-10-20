L = [10, 20, 30]
L[1 : 1] = [15]
L.insert(3, 25)
L.append(35)
print(L)

L = []
for i in range(5):
    num = int(input("숫자 입력: "))
    L.append(num)
    # L.insert(i, num)
    # L += [num]
    # L[i:i] = [num]
print(L)

print(L.index(10))
print(L.count(10))
L.sort() # 오름차순
print(L)
L.sort(reverse=True) # 내림차순
print(L)
L2 = sorted(L, reverse=True) # 원본 보류
print(L)

L = ['blueberry', 'banana', 'apple']
L.sort()
print(L)

L = ['123', '34', '2345']
L.sort()
print(L)
L.sort(key=int)
print(L)
L.clear() # list 요소 비우기
print(L)

del L # list 삭제

