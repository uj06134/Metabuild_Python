L = list(range(10))
print(L)
print(L[0:5])
print(L[1::3])
print(L[0::2])
print(L[1::2])
print(L[::-2])

L = ['a', 1, 'b', 2]
print(L)

L[1:3] = [1, 2, 3]
print(L)
L[1:2] = [50]
print(L)
L[1] = 50
print(L)
L[1] = [1, 2, 3]
print(L)

del(L[1])
print(L)

L2 = L
print(L2 == L)

