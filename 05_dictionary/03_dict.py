person = {}
total = 0
while True:
    name = input("이름입력: ")
    if name == "quit":
        break
    age = int(input("나이입력: "))
    person[name] = age
print(person)
print(sum(person.values()))

while True:
    search_name = input("이름 검색: ")
    if search_name == "stop":
        break
    search_name = search_name.lower()
    if search_name in person.keys():
        print(person.get(search_name))
    else:
        print("찾는 나이는 없습니다")
