f = open("gugudan.txt","w")
for i in range(1, 10):
    data = f"3 * {i} = {3 * i}\n"
    f.write(data)
f.close()

print('console 구구단 출력1')
f = open("gugudan.txt","r")
s = f.read()
print(s)
f.close()

print('console 구구단 출력2')
f = open("gugudan.txt","r")
while True:
    line = f.readline()
    if line == "":
        break
    print(line,end='')
f.close()

print('console 구구단 출력3')
f = open("gugudan.txt","r")
lines = f.readlines()    # readlines() → 모든 줄을 리스트 형태로 읽기
print(type(lines))
for line in lines:
    print(line, end='')
# print(lines)
f.close()
