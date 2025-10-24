import numpy as np

arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
print(arr[0,0], arr[1][1], arr[2][0])
# Fancy Indexing (팬시 인덱싱)
print(arr[[0,1,2],[0,1,0]])     # → 첫 번째 리스트 [0,1,2]는 '행 인덱스' 목록
                                # → 두 번째 리스트 [0,1,0]은 '열 인덱스' 목록
                                # 즉, 다음과 같은 원소들을 각각 선택함:
                                # arr[0,0] → 1
                                # arr[1,1] → 4
                                # arr[2,0] → 5
print(arr[[0,2]])
print(arr[np.arange(3),[0,1,0]])
print(arr[arr>2])
