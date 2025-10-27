class Movie:
    def __init__(self, title, name, rank):
        self.title = title
        self.name = name
        self.rank = rank

    def __str__(self):
        return f"영화명: {self.title}  |  감독: {self.name}  |  영화등급: {self.rank}"

class MovieManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, name, rank):
        movie = Movie(title, name, rank)
        self.movies.append(movie)
        print("영화가 등록되었습니다.")

    def show_movies(self):
        print("전체 영화 목록:")
        for movie in self.movies:
            print(movie)

    def search_movie(self, search_name):
        found_list = []
        for movie in self.movies:
            if search_name in movie.name:
                found_list.append(movie)

        if found_list:
            for movie in found_list:
                print(movie)
        else:
            print(f"'{search_name}' 영화를 찾을 수 없습니다.")

    def delete_movie(self, delete_title):
        flag = False
        for movie in self.movies:
            if movie.title == delete_title:
                self.movies.remove(movie)
                print(f"{delete_title} 영화가 삭제되었습니다.")
                flag = True

        if not flag:
            print(f"'{delete_title}' 영화를 찾을 수 없습니다.")

    def update_movie(self, update_title, update_rank):
        for movie in self.movies:
            if movie.title == update_title:
                movie.rank = update_rank
                print(f"'{update_title}' 영화등급이 수정되었습니다.")

    def file_write(self):
        with open("movies.txt", "w", encoding="utf-8") as f:
            for movie in self.movies:
                f.write(f"{movie.title},{movie.name},{movie.rank}\n")
        print("텍스트 파일로 저장되었습니다.")

    def file_read(self):
        try:
            with open("movies.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    title, name, rank = line.split(",")
                    self.movies.append(Movie(title, name, rank))
            print("파일에서 데이터가 불러와졌습니다.")
        except FileNotFoundError:
            print("파일이 없습니다")

if __name__ == "__main__":
    manager = MovieManager()
    manager.file_read()
    while True:
        print("영화 관리 시스템")
        print("1. 영화 등록")
        print("2. 전체 영화 보기")
        print("3. 영화 검색")
        print("4. 영화 삭제")
        print("5. 영화 등급 수정")
        print("6. 파일 저장")
        print("7. 종료")

        try:
            menu = int(input("메뉴 선택 (1~7): "))
            if menu not in range(1, 8):
                raise ValueError
        except ValueError:
            print("올바른 메뉴 번호를 입력하세요.")
        else:
            if menu == 1:
                title = input("영화명: ")
                name = input("감독: ")
                while True:
                    try:
                        rank = int(input("영화등급-숫자1자리또는 2자리(예: 7, 15): "))
                        if rank < 0 or rank > 99:
                            raise ValueError
                        break
                    except ValueError:
                        print("영화등급은 숫자 또는 영문만 입력 가능합니다.")

                manager.add_movie(title, name, rank)

            if menu == 2:
                manager.show_movies()

            if menu == 3:
                search_name = input("검색할 감독명 키워드: ")
                manager.search_movie(search_name)

            if menu == 4:
                delete_title = input("삭제할 영화명: ")
                manager.delete_movie(delete_title)

            if menu == 5:
                flag = False
                update_title = input("수정할 영화명: ")
                for movie in manager.movies:
                    if update_title in movie.title:
                        while True:
                            try:
                                update_rank = int(input("새 영화등급-숫자1자리또는 2자리(예: 7, 15): "))
                                if update_rank < 0 or update_rank > 99:
                                    raise ValueError
                                break
                            except ValueError:
                                print("영화등급은 숫자 또는 영문만 입력 가능합니다.")
                        manager.update_movie(update_title, update_rank)
                        flag = True
                if not flag:
                    print(f"'{update_title}' 영화를 찾을 수 없습니다.")

            if menu == 6:
                manager.file_write()

            if menu == 7:
                print("프로그램 종료")
                break




