import numpy as np
a = np.arange(5)
print(a)

for b in np.arange(5):
    print(b)

c = np.arange(20, 7, -1)
print(c)

d = np.arange(2*3).reshape(2,3)
print(d)

e = np.arange(3*2).reshape(3,2)
print(e)

de = np.matmul(d, e)
print(de)
# = A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0] = (0)*0 + (1)*2 + (2)*4 = 0 + 2 + 8 = 10
# = A[0][0]*B[0][1] + A[0][1]*B[1][1] + A[0][2]*B[2][1] = (0)*1 + (1)*3 + (2)*5 = 0 + 3 + 10 = 13
# = A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0] = (3)*0 + (4)*2 + (5)*4 = 0 + 8 + 20 = 28
# = A[1][0]*B[0][1] + A[1][1]*B[1][1] + A[1][2]*B[2][1] = (3)*1 + (4)*3 + (5)*5 = 3 + 12 + 25 = 40

f = np.array([0,1,'2','abc',True,'True'])
print(f)

arr1 = np.zeros(3)
print(arr1)

arr2 = np.zeros((2,3))
print(arr2)

arr3 = np.ones((2,3))
print(arr3)

arr4 = np.full((2,3), 7)
print(arr4)

arr5 = np.eye(3)
print(arr5)