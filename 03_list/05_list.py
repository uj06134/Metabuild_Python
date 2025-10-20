L = list(range(10))
print(L)

L = [i for i in range(10)]
print(L)

score = [90, 25, 67, 45, 80]
print("합계:", sum(score))
print("최댓값:", max(score))
print("최솟값:", min(score))

for i in enumerate(score):
    print(i)

for i,j in enumerate(score, start=1): # 1부터 시작
    print(i,j)