import Ex04

s1 = Ex04.Service("슬기")
s1.show()

from Ex04 import *
s1 = Service("조이")
s1.show()

import Ex04 as e

s1 = e.Service("아이린")
s1.show()

print('------------')
from Ex02 import *

s1 = Student(10)
print(s1.name, s1.age)
