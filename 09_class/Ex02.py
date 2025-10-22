class Student:
    name = "철수"

    # 생성자
    def __init__(self, age):
        print('init:', self)
        self.age = age

if __name__ == '__main__':
    s1 = Student(10)
    s2 = Student(20)
    print(s1.name, s1.age)
    print(s2.name, s2.age)
