t1 = ()
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1,)
t5 = 1,
t6 = (1)
t7 = 1
print(t1,type(t1))
print(t2,type(t2))
print(t3,type(t3))
print(t4,type(t4))
print(t5,type(t5))
print(t6,type(t6))
print(t7,type(t7))

t = (1, 2, 3)
print(t[0])

t2 = t + ('kim', 'lee')
print(t2)

t2 = t , ('kim', 'lee')
print(t2)

x,y,z = 1, 2, 3
print(x,y,z)

x, y = y, x
print(x,y)

p, q, r = t
print(p,q,r)

t = (1, 2, 3)
L = list(t) # 리스트 변환
L[0] = 99 # 값 바꾸기
t3 = tuple(L) # 튜플로 재변환
print(t3)

print("id: %s pw: %s" % ("kim",1234))