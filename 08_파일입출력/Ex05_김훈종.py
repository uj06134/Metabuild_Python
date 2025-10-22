# 연도에 해당하는 txt 파일 생성
# ex) 1990.txt, 1988.txt ..
fr = open("file/members.txt", "r", encoding="utf-8")

for line in fr.readlines():
    arr = line.split(',')
    year = arr[1].split('-')[0]
    fw = open(f"{year}.txt", 'a', encoding="utf-8")
    fw.write(line)
    fw.close()
fr.close()
