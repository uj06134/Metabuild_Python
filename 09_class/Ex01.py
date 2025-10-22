class Person:
    # class 변수
    last_name = "kim"
    # class 안에 들어가는 메서드는 매개변수가 반드시 필요 (보통은 self)
    def set_name(self,x):
        print('self:', self)
        self.fullname = self.last_name + " " +x
    def set_age(self,y):
        self.age = y
    def display(self):
        print(self.fullname,'/',self.age)
# 객체 생성
p1 = Person()
p2 = Person()
print(p1)
print(p1.last_name)
print(Person.last_name)
p1.set_name('hoon jong')
p2.set_name('jung ryun')
p1.set_age(30)
p2.set_age(40)
p1.display()
p2.display()
