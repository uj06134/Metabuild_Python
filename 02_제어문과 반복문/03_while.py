total = 0
i=0
while i < 11:
    total = total + i
    i += 1

print(total)
print("------------------")
i=1
while True:
    if i>5:
        break
    print(i)
    i += 1
print("------------------")
total = 0
count = 0
while True:
    score = int(input("숫자 입력: "))
    if score < 0:
        break
    count = count + 1
    total = total + score
print("합계:", total)
print("평균:", total / count)
print("평균: %.2f" % (total / count))
print("평균:{: .2f}" .format(total / count))
print("평균:", round(total / count, 2))
