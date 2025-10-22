class Box:
    def __init__(self, num):
        self.num1 = num
        self.num2 = num

    # 연산자 오버로딩 (왼쪽 피연산자)
    def __add__(self, num):
        self.num1 += num
        return f"더하기(__add__): {self.num1}"

    # 연산자 오버로딩 (오른쪽 피연산자)
    def __radd__(self, num):
        self.num1 += num
        return f"더하기(__radd__): {self.num1}"

    # 연산자 오버로딩 (왼쪽 피연산자)
    def __sub__(self, num):
        self.num1 -= num
        return f"뺴기(__sub__): {self.num1}"

b1 = Box(10)
print(b1.num1)
print(b1.num2)
print(b1.num1 + b1.num2)
# 객체-숫자 간 연산
print(b1 + 30)
print(40 + b1)
print(b1 - 70)