import os
print(os.getcwd())
# os.chdir('./../')
print(os.listdir('.'))
print(os.listdir('..'))

# os.rename('a.txt', 'c.txt')
# os.rename('c.txt', 'my/d.txt')

# os.remove('b.txt')
# os.remove('my') # 폴더안에 확장자가 있으면 remove 불가

import shutil
# shutil.rmtree('my')
shutil.copy('a.txt', 'b.txt')