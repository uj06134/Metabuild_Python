import numpy as np
a = 100
print(a)
print(type(a))
print('--------------')

b = [1,2,3,4]
print(b)
print(type(b))
print(len(b))
print('--------------')

c = [[1,2,3,4],[5,6,7,8]]
print(c)
print(type(c))
print(len(c))

for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j], end=' ')
    print()
print('--------------')

d = np.array(200)
print(d)
print(type(d))
print('--------------')

e = np.array([1,2,3])
print(e)
print(e.ndim)
print(e.shape)
print('--------------')

f = np.array([[1,2,3,4],[5,6,7,8]])
print(f[1][0])
print(f.ndim)
print(f.shape)

for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        print(f[i][j], end=' ')
    print()
print('--------------')

g = np.array([[1,2,3,4]])
print(g)
print(g.ndim)
print(g.shape)
print('--------------')

h= np.array(c)
print(h)
print(type(h))
print(h.ndim)
print(h.shape)
