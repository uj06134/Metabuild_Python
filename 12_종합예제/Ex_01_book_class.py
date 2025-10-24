import re

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"제목: {self.title}, 저자: {self.author}, 가격: {self.price}원"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        new_book = Book(title, author, price)
        self.books.append(new_book)
        print("도서가 등록되었습니다.")

    def show_all_books(self):
        if not self.books:
            print("등록된 도서가 없습니다.")
        else:
            print("\n전체 도서 목록:")
            for book in self.books:
                print(book)

    def find_book(self, search_title):
        found_list = []
        for book in self.books:
            if search_title.lower() in book.title.lower():
                found_list.append(book)

        if found_list:
            for book in found_list:
                print(book)
        else:
            print(f"'{search_title}'에 해당하는 도서를 찾을 수 없습니다.")

    def delete_book(self, delete_title):
        flag = False
        for book in self.books:
            if book.title.lower() == delete_title.lower():
                self.books.remove(book)
                print(f"'{delete_title}' 도서가 삭제되었습니다.")
                flag = True

        if not flag:
            print(f"'{delete_title}'에 해당하는 도서를 찾을 수 없습니다.")

    def update_book(self, update_title):
        found = False
        for book in self.books:
            if update_title.lower() == book.title.lower():
                found = True

                while True:
                    new_price = input("수정할 가격 입력 (3~5자리 숫자): ")
                    pattern = re.compile(r'^\d{3,5}$')
                    if not pattern.match(new_price):
                        print("가격은 3자리에서 5자리 숫자만 입력 가능합니다.")
                        continue
                    book.price = int(new_price)
                    print(f"'{book.title}' 도서의 가격이 수정되었습니다.")
                    break

        if not found:
            print(f"'{update_title}'에 해당하는 도서를 찾을 수 없습니다.")

    def file_write(self):
        with open("books.txt", "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.price}\n")
        print("텍스트 파일로 저장되었습니다.")

    def file_read(self):
        try:
            with open("books.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    title, author, price = line.split(",")
                    self.books.append(Book(title, author, price))
            print("저장된 파일을 불러왔습니다.")
        except FileNotFoundError:
            print("저장된 파일이 없습니다. 새로 시작합니다.\n")

def main():
    manager = BookManager()
    manager.file_read()

    while True:
        print("\n[도서 관리 시스템]")
        print("1. 도서 등록")
        print("2. 전체 도서 보기")
        print("3. 도서 검색")
        print("4. 도서 삭제")
        print("5. 도서 가격 수정")
        print("6. 파일 저장")
        print("7. 종료")

        try:
            menu = int(input("메뉴 선택 (1~7): "))
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if menu == 1:
            title = input("도서 제목: ")
            author = input("저자: ")
            while True:
                try:
                    price = int(input("가격: "))
                    break
                except ValueError:
                    print("가격은 숫자로 입력하세요.")
            manager.add_book(title, author, price)

        elif menu == 2:
            manager.show_all_books()

        elif menu == 3:
            search_title = input("검색할 도서 제목 입력: ")
            manager.find_book(search_title)

        elif menu == 4:
            delete_title = input("삭제할 도서 제목 입력: ")
            manager.delete_book(delete_title)

        elif menu == 5:
            update_title = input("수정할 도서 제목 입력: ")
            manager.update_book(update_title)

        elif menu == 6:
            manager.file_write()

        elif menu == 7:
            print("프로그램 종료")
            break

if __name__ == "__main__":
    main()