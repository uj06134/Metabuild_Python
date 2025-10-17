print("입력: ", end="")
a = input()
print("a:", a)

b = int(input("입력: "))
print("b:", b)

sum = int(a) + b
print(a, "+", b, "=",sum)

c = float(input("키 입력: "))
print("c:", c)

print("나이는 {}살이고 키는 {}입니다".format(a,c))
print("나이는 {0}살이고 키는 {1}입니다".format(a,c))   # 인덱스 0 → a, 1 → c
print("나이는 {x}살이고 키는 {y}입니다".format(x=a,y=c))