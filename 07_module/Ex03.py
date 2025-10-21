# 내장 함수
print(round(2.8))
print(sum((10,20)))
# math 모듈
import math
print(math.pi)
print(math.factorial(5))

from math import *
print(sqrt(5))

from math import factorial as f
print(f(3))

print(abs(-3))
print(max(-3, 4, 100))
print(pow(3, 4))

import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())

from datetime import *
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print('%s년 %s월 %s일' % (now.year, now.month, now.day))
print('%d년 %d월 %sd' % (now.year, now.month, now.day))

def weekday_today(now):
    year = now.year
    month = now.month
    day = now.day
    weekday = now.weekday()
    week = ['월', '화', '수', '목', '금', '토', '일']
    return f"{year}년 {month}월 {day}일은 {week[weekday]}요일 입니다."

print(weekday_today(now))