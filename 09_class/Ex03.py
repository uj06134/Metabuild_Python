class Bank:
    rate = 0.03
    def __init__(self, money):
        self.money = money

    def calcuate(self):
        self.total_money = self.money + (self.money * self.rate)

    def show(self):
        self.calcuate()
        print(self.total_money)

b1 = Bank(10000)
b2 = Bank(30000)

b1.show()
b2.show()
