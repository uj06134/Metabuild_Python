x = 3
y = 0
L = [1,2,3]
try:
    print(x/y) # - ZeroDivisionError
    print(L[3]) # - IndexError
    print('a' + 2) # - TypeError
    print(int('a')) # - ValueError
except:   # 예외 발생
    pass
else:     # 예외 없음
    pass
finally:  # 항시 실행
    print('finally')

try:
    print('a' + 2) # - TypeError
except TypeError as e:
    print(e)

try:
    print(int('a')) # - ValueError
except ValueError as e:
    print(e)