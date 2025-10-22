class Super:
    def __init__(self):
        print('Super 생성자')
    def show(self):
        print('Super show')

class Sub():
    def __init__(self):
        print('Sub 생성자')
    def show(self):
        print('Sub show')
# 상속
class Sub2(Super):
    def __init__(self):
        Super.__init__(self)   # 1. 부모 클래스의 생성자를 직접 호출
                               # 상속받았다고 해서 자동 호출되지 않음
        # super().__init__()   # 2. super()로 부모 클래스의 생성자 호출
        print('Sub2 생성자')
    def show(self):
        Super.show(self)
        # super().show()
        print('Sub2 show')

sp1 = Super()
sb1 = Sub()
sb2 = Sub2()
print('---------------')
sp1.show()
sb1.show()
sb2.show()
