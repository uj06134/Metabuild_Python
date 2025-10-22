class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def show(self):
        super().show()
        print(self.position, self.salary)

p1 = Person('보검', 30)
p2 = Person('아이유', 40)
e1 = Employee('태연', 50, '대리', 300)
e2 = Employee('수영', 20, '사원', 200)

p1.show()
p2.show()
e1.show()
e2.show()