import numpy as np

a = np.array([-1,3,2,6])
b = np.array([3,6,1,2])
print(a+b)

ab = np.matmul(a,b) # 각 방끼리 곱한후 총 합계
print(ab)           # -3 + 18 + 2 + 12 = 29

A = np.reshape(a,(2,2))
print(A)

B = b.reshape([2,2])
print(B)

AB = np.matmul(A,B)
print(AB)

# 결과 행렬 AB = A × B
# 각 원소의 계산 과정:
# AB[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0] = (-1)*3 + (3)*1 = 0
# AB[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1] = (-1)*6 + (3)*2 = 0
# AB[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0] = (2)*3 + (6)*1 = 12
# AB[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1] = (2)*6 + (6)*2 = 24

# np.transpose: 행렬을 전치(transpose) 하는 함수
# 행(row)과 열(column) 을 서로 바꿔주는 연산
result = np.transpose(AB)
# result = AB.T
print(result)