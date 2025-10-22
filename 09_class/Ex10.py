class Lion:
    def __init__(self):
        print('Lion')
    def bite(self):
        print('Lion bite')
    def cry(self):
        print('Lion cry')

class Tiger:
    def __init__(self):
        print('Tiger')
    def jump(self):
        print('Tiger jump')
    def cry(self):
        print('Tiger cry')
    def play(self):
        print('Tiger play')

class Liger(Tiger, Lion):
    def play(self):
        print('Liger play')

l = Liger() # Liger에는 __init__이 없기 때문에 상속 순서상 첫 번째 부모인 Tiger의 생성자가 호출됨
l.play() # Liger 자신의 play() 호출
l.jump() # Liger에는 jump() 없음 → Tiger 클래스의 jump() 호출
l.bite() # Tiger에는 bite() 없음 → 다음 부모 Lion의 bite() 호출
l.cry()  # cry()는 Tiger와 Lion 둘 다 있음
         # MRO 순서상 Tiger가 먼저이므로 Tiger의 cry() 실행