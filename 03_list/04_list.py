L=[
    ['apple', 'banana'],
    [10, 20, 30]
]
print(L)
print(L[0][0])
print(L[1])
print("------------------")
for i in range(len(L)):
    for j in range(L[i].__len__()):
        print(L[i][j], end=' ')
    print()
print("------------------")
for i in L:
    for j in i:
        print(j, end=' ')
    print()