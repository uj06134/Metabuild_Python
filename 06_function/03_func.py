x = 10 # 전역 변수
def func():
    x=30 # 지역 변수 (지역 변수가 없으면 전역변수가 우선 순위)
    print('func x:', x)

func()
print('x:', x)
print('------------------')
y = 10
def func2(y):
    y = y * y
    global k
    k = 20
    print('func2 y:',y)

func2(y)
print('y:', y)
print('k', k)
