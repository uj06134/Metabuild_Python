class Address :
    def __init__(self):
         self.city = ""
         self.street = ""

    def setAddress(self, city, street):
        self.city = city
        self.street = street

    def showAddress(self):
        return f"{self.city} {self.street}"

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = Address() # Address 객체를 포함
        
    def setAddress(self, city, street):
        # self.address.city = city
        # self.address.street = street
        self.address.setAddress(city, street) # Address 객체의 메서드를 이용해 주소 설정

    def showStudent(self):
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"주소: {self.address.showAddress()}")
s1 = Student("서현", 30)
s1.setAddress("서울", "서초구")
s1.showStudent()