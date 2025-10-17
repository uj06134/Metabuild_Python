su = 11
if su % 2 == 0:
    print(su , end=' ')
    print("짝수")
else:
    print(su , end=' ')
    print("홀수")
    
# 학점 입력
score = int(input("점수 입력: "))
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")

if score >= 80:
    print("Pass")
else:
    print("Fail")

result = "Pass" if score >= 80 else "Fail"
print(result)

result2 = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(result2)