try:
    a = int(input('숫자1: '))
    b = int(input('숫자2: '))
except ValueError:
    print("숫자로 입력하세요")
else:
    print('a + b =', a + b)

try:
    with open("a.txt", "r", encoding="utf-8") as r:
        print(r.read())
except FileNotFoundError:
    print("파일이 없습니다")

try:
    fr = open("b.txt", "r", encoding="utf-8")
    read = fr.read()
except FileNotFoundError:
    print("파일이 없습니다")
    fw = open("b.txt", "w", encoding="utf-8")
    fw.write("Hi")
    fw.close()
else:
    print(read)
    fr.close()

try:
    a = int(input("숫자1: "))
    b = int(input("숫자2: "))

    if a<0 or b<0:
        raise ValueError("음수 존재") # 강제로 에러 발생
except ValueError as e:
    print("음수 입력 불가능", e)
else:
    print("두 수 모두 양수")
