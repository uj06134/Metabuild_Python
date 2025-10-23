book_list = []
while True:
    print("[도서 관리 시스템]")
    print(""
          "1. 도서 등록\n"
          "2. 전체 도서 보기\n"
          "3. 도서 검색\n"
          "4. 도서삭제\n"
          "5. 도서 가격 수정\n"
          "6. 파일 저장\n"
          "7. 종료"
          )
    try:
        menu = int(input("메뉴 선택 (1~7) :"))
        if menu not in range(1, 8):
            raise ValueError
    except ValueError:
        print("1 ~ 7사이 입력")
    else:
        if menu == 1:
            title = input("도서 제목: ")
            author = input("저자: ")
            while True:
                try:
                    price = int(input("가격: "))
                except ValueError:
                    print("가격은 숫자로 입력하세요")
                    continue
                break
            book = {"제목": title, "저자": author, "가격": price}
            book_list.append(book)
            print("책이 등록되었습니다")
        elif menu == 2:
            if len(book_list)==0:
                print("등록된 도서가 없습니다.")
            else:
                print("\n전체 도서 목록:")
                for book in book_list:
                    print(f"제목: {book['제목']} | 저자: {book['저자']} | 가격: {book['가격']}원")
        elif menu == 3:
            search_keyword = input("검색할 도서 제목 키워드: ")
            found = False
            print(f"'{search_keyword}'검색 결과:")
            for book in book_list:
                if search_keyword in book["제목"]:
                    print(f"제목: {book['제목']} | 저자: {book['저자']} | 가격: {book['가격']}원")
                    found = True
            if not found:
                print(f"'{search_keyword}'에 해당하는 도서를 찾을 수 없습니다.")
        elif menu == 4:
            delete_keyword = input("삭제할 도서 제목: ")
            found = False
            for book in book_list:
                if delete_keyword == book["제목"]:
                    book_list.remove(book)
                    print(f"'{delete_keyword}' 도서가 삭제되었습니다.")
                    found = True
            if not found:
                print(f"'{delete_keyword}' 도서를 찾을 수 없습니다.")
        elif menu == 5:
            change_keyword = input("수정할 도서 제목: ")
            found = False
            for book in book_list:
                if change_keyword == book["제목"]:
                     try:
                        change_price = int(input("수정할 가격(3~5자리 숫자)"))
                     except (ValueError, FileNotFoundError) as e:
                        print(e)

                    found = True
            if not found:
                print(f"'{change_keyword}' 도서를 찾을 수 없습니다.")
        elif menu == 6:
            pass
        elif menu == 7:
            pass