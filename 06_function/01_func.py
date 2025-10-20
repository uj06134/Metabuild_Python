def add(a, b) :
    return a + b

result1 = add(10, 20)
print(result1)

result2 = add([1,2,3], [4,5,6])
print(result2)

def func():
    pass

result = func()
print(result)

def func2(x,y=0,z=0):
    return x+y+z

print(func2(1))
print(func2(1, 2))
print(func2(1, 2, 3))
