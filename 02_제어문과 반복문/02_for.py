for i in range(1,11):
    print(i)
print("------------------")
for i in range(2,11,2):
    print(i)
print("------------------")
total = 0
for i in range(1,11):
    total += i
print("total:", total)
print("total: %d" % total)
print("total: " + str(total))
print("total: {}".format(total))
print("total: {0}".format(total))
print("total: {sum}".format(sum = total))
print("------------------")
even_total = 0
odd_total = 0
for i in range(2,11,2):
    even_total += i
print("1~10 짝수의 합계:", even_total)

for i in range(1,11,2):
    odd_total += i
print("1~10 홀수의 합계:", odd_total)
print("------------------")
even = 0
odd = 0
for i in range (1, 11) :
    if i % 2 == 0 :
        even += i
    else:
        odd += i
print("1~10 짝수의 합계: {}".format(even))
print("1~10 홀수의 합계: %d" % odd)
print("------------------")
for i in range(1,11):
    if i == 5:
        continue
    print(i)
print("------------------")
for i in range(2,10):
    print(str(i) + "단")
    for j in range(1,10):
        print(f"{i} * {j} = {i * j}")
    print("------------------")

num = int(input("숫자 입력: "))
for i in range(1,num+1):
    print(i * "*")
