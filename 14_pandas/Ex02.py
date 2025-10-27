import pandas as pd
import numpy as np

s = pd.Series([100,200,300,400], index=['국어','영어','수학','과학'])
print(s)

# 수정
s['과학'] = 450
print(s)
# 추가
s['미술'] = 250
print(s)

# 300이상
print(s[s.values >= 300])

# 200~400
print(s[(s.values >= 200) & (s.values <= 400)])

# 인덱스 기준 정렬
print(s.sort_index())

# value 내림차순 정렬
print(s.sort_values(ascending=False))

# 최댓값, 최솟값, 합계, 평균
print(np.max(s))
print(np.min(s))
print(np.sum(s))
print(np.mean(s))

# 
subject = ['국어', '영어', '체육']
s2 = s.reindex(subject,fill_value=0)
print(s2)
