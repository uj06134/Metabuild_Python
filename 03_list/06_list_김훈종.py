students = [
    ["kim", 90, 10],
    ["park", 80, 30],
    ["choi", 70, 50],
    ["jung", 60, 70],
    ["hong", 50, 90],
]

# list 뒤에 평균, 학점 추가 ex) ["kim", 90, 10, 50, 'B']
# 이름기준 오름차순 정렬
# 이름을 대문자로 변경

for i in range(len(students)):
    students[i][0] = students[i][0].upper()
    avg = (students[i][1] + students[i][2]) / 2
    students[i].append(avg)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    students[i].append(grade)
    students.sort()
print(students)
