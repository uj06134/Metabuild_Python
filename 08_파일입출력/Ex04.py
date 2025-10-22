fr = open("file/sungjuk.txt", "r", encoding="utf-8")
fw = open("sungjuk_result.txt", 'w', encoding="utf-8")

line = fr.readline() #  이름	국어	영어	수학\n
fw.write(line)
pos = fw.tell()
print(pos)
fw.seek(pos-2)
fw.write("\t합계\n")

for line in fr.readlines():
    total = 0
    print(line)
    arr = line.split()
    # print(arr) # list
    for i in range(1,len(arr)):
        print(arr[i])
        total += int(arr[i])
    fw.write(line)
    pos = fw.tell()
    fw.seek(pos - 2)
    fw.write("\t"+str(total)+"\n")
fr.close()
fw.close()