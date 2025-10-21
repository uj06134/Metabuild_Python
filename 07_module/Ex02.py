import Ex01
Ex01.abc()
Ex01.xyz()
print('------------')
import Ex01 as e
e.abc()
e.xyz()
print('------------')
from Ex01 import abc, xyz
abc()
xyz()
print('------------')
from Ex01 import *
abc()
xyz()
print('------------')
from myPkg.Ex01 import *
print(add(10,20))
