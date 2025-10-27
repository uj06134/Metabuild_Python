# 41~100점 정수난수 5행 4열(5명 4과목)
# 0열 국어
# 1열 영어
# 2열 수학
# 3열 과학
import numpy as np
arr = np.random.randint(41, 101, (5,4))
print(arr)

# 학생별 총점
stu_total = np.sum(arr, axis=1)
print("학생별 총점:", stu_total)

# 학생별 평균
stu_avg = np.average(arr, axis=1)
stu_avg = np.round(stu_avg, 3)
print("학생별 평균:", stu_avg)

# 과목별 총점
sub_total = np.sum(arr, axis=0)
print("과목별 총점:", sub_total)

# 과목별 평균
sub_avg = np.average(arr, axis=0)
sub_avg = np.round(sub_avg, 2)
print("과목별 평균:", sub_avg)

# 과목별 최댓값
sub_max = np.max(arr, axis=0)
print("과목별 최댓값:",sub_max)

# 과목별 최솟값
sub_min = np.min(arr, axis=0)
print("과목별 최솟값:", sub_min)

# 학생별 평균 >= 70이면 합격
name = np.array(['사람1', '사람2', '사람3', '사람4', '사람5'])
print("70점이상 합격자(T or F):", stu_avg >= 70)
print(name[stu_avg >= 70])


# 전체 평균
print("전체 평균:", np.average(arr))
print(np.round(np.average(arr), 2))

# 영어 점수
print("영어 점수:", arr[:, 1])

# 국어>=70, 수학>=80
print("국어 점수 70점이상, 수학점수 80점이상인 학생:")
for i in range(arr.shape[0]):
    if arr[i][0] >= 70 & arr[i][2] >= 80:
        print(arr[i])

cond = (arr[:,0] >= 70) & (arr[:,2] >= 80)
print(arr[cond])