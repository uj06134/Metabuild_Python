d = {}
while True:
    try:
        title = input("제목 입력: ")
        if len(title) < 3 or len(title) > 5:
            raise ValueError
    except:
        print("제목은 3~ 5글자로 입력")
        continue
    while True:
        try:
            price = int(input("가격: "))
        except ValueError:
            print("가격은 숫자로 입력하세요")
            continue
        d[title] = price
        break
    answer = input("계속?: ")
    if answer == "n":
        break

print(d)