import os

# "w" 모드: 쓰기(write) 모드
#  - 파일이 없으면 새로 생성
#  - 파일이 이미 있으면 기존 내용을 모두 지우고 새로 작성
open("file/test.txt", "w").close()
f = open("file/test.txt", "w", encoding="utf-8")
f.write("hello world\n")
f.write("하이")
f.close()

# "a" 모드: 추가(append) 모드
#  - 파일이 없으면 새로 생성
#  - 파일이 있으면 기존 내용은 유지하고, 새 내용이 뒤에 추가됨
open("file/test.txt", "a").close()

# "r" 모드: 읽기(read) 모드
#  - 파일이 반드시 존재해야 함 (없으면 오류 발생)
#  - 파일의 내용을 읽을 때 사용
f = open("file/test.txt", "r", encoding="utf-8")
s = f.read()
print(s)
f.close()

# with문: 파일을 자동으로 열고 닫아주는 구문
# - 파일 작업이 끝나면 자동으로 close() 실행됨
with open("file/test.txt", "w", encoding="utf-8") as f:
    f.write("hello world\n")
    f.write("하이")


f= open("file/test.txt", "r", encoding="utf-8")
pos = f.tell()
print('pos:', pos)
s = f.read()
print(s)
f.seek(10)
pos2 = f.tell()
print('pos2:', pos2)
f.close()