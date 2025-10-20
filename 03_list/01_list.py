a=1
print(type(a))

b="123"
print(type(b))

c=True
print(type(c))

L = [10, 20, 30]
print(type(L))
print(L)
print(L[0])
print(L[-1])
print(len(L))
print(L.__len__())

for i in L:
    print(i)

for i in range(0,len(L)):
    print(L[i])

print(L+L)
print(L*2)
