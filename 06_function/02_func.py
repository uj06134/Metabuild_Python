print('--------func1--------')
def func(*args):
    for i in args:
        print(i, end="/")
    print()

func()
func(1,2)
func([1,2,3], (4,5,6))
func("apple", "banana", "orange")
print('--------func2--------')

def func2(a,b, *args):
    print('a', a)
    for i in args:
        print(i, end="/")
    print()

func2(1, 2)
func2([1,2,3], (4,5,6))
func2("apple", "banana", "orange")

print('--------func3--------')
tp = (1,2,3)
def func3(a,b,c) :
    print('a', a)

func3(tp[0], tp[1], tp[2])

print('--------func4--------')
def func4(a,b,c) :
    print(a,b,c)

func4(*tp)
print('--------func5--------')
d = {'a':10,'b':20,'c':33}
def func5(a,b,c) :
    print(a,b,c)

func4(*d)
func5(**d)
print('--------func6--------')
def func6(a):
    if a > 1:
        return a + func6(a-1)
    elif a==1 :
        return 1
    return None

print(func6(5))
print('--------func7--------')
def func7(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 100)

print(func7('a'))
print(func7('b'))
print(func7('c'))
