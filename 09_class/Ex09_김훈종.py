class Product:
    def __init__(self, fruit, price):
        self.fruit = fruit
        self.price = price
    def printProduct(self):
        print(f"{self.fruit}/{self.price}원")

class Cart:
    def __init__(self):
        self.items = []  # p1,3 p2,4

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart() # 포함

    def addCart(self, product, count):
        self.cart.items.append((product, count))

    def checkout(self):
        print(f"{self.name} 결제정보")
        total = 0
        for item, count in self.cart.items:
            print(f"{item.fruit} * {count} = {item.price * count}원")
            total += item.price * count
        print(f"총합: {total}원")

p1 = Product("사과", 1000)
p2 = Product("포도", 2000)
p3 = Product("딸기", 3000)

# ex) 사과/1000원
p1.printProduct()
p2.printProduct()
p3.printProduct()

# cart = Cart 포함
c1 = Customer("수영")
c2 = Customer("정국")

c1.addCart(p1, 3)
c1.addCart(p2, 4)

c2.addCart(p2, 2)
c2.addCart(p3, 5)

# 수영 결제정보 (c1)
# 사과 * 3 = 3000원
# 포도 * 4 = 8000원
# 총합 : 11000원
c1.checkout()
c2.checkout()
