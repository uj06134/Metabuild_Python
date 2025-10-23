d = {}
while True:
    print("----- Menu Select -----\n"
          "1. 전체 조회\n"
          "2. 추가\n"
          "3. 수정\n"
          "4. 삭제\n"
          "0. 종료")
    menu = int(input("번호 선택: "))
    if menu < 0 or menu > 4:
        print("잘못 입력")
    if menu == 1:
        if len(d) == 0:
            print("등록된 데이터가 없습니다.")
        else:
            print("제목\t가격")
            for k, v in d.items():
                print(f"{k}\t{v}")
    elif menu == 2:
        title = input("제목: ")
        while True:
            try:
                price = int(input("가격: "))
            except ValueError:
                print("가격은 숫자로 입력하세요")
                continue

            break
        d[title] = price
        continue
    elif menu == 3:
        while True:
            try:
                find_title = input("수정할 제목: ")
                if len(find_title) > 5:
                    raise ValueError("제목은 5글자 이하만 가능합니다.")
                if find_title not in d:
                    raise FileNotFoundError("파일에 없는 제목입니다. 다시 입력하세요.")
            except (ValueError, FileNotFoundError) as e:
                print(e)
                continue
            change_price = int(input("수정할 가격: "))
            d[find_title] = change_price
            print("수정 완료")
            break
    elif menu == 4:
        while True:
            try:
                delete_title = input("삭제할 제목: ")
                if delete_title not in d:
                    raise FileNotFoundError("파일에 없는 제목입니다. 다시 입력하세요.")
            except FileNotFoundError as e:
                print(e)
                continue
            del(d[delete_title])
            print("삭제 완료")
            break

    elif menu == 0:
        print("종료")
        break

