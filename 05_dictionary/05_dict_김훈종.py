score = {
    '윤아': {'국어':65, '수학':92, '영어':74},
    '정국': {'국어':15, '수학':12, '영어':13},
    '태연': {'국어':41, '수학':25, '영어':78},
    '보검': {'국어':75, '수학':33, '영어':15}
}

# 학생별 평균을 구하고 평균이 70점이상인 학생 ex) {'윤아':평균, '정국':평균}
# 평균 정렬: 내림차순
avg = {}
for name in score.keys():
    total = sum(score[name].values())
    sub_count = len(score[name])
    avg[name] = round(total/sub_count,2)

sorted_name = sorted(avg, key=avg.get, reverse=True)
sorted_avg = {}
for name in sorted_name:
    sorted_avg[name] = avg[name]

print(sorted_avg)
# 각 과목에서 최고점 학생
top = {}
for subject in list(score.values())[0]:
    max_score = 0
    top_name = ''
    for name in score:
        if score[name][subject] > max_score:
            max_score = score[name][subject]
            top_name = name
    top[subject] = top_name

print(top)