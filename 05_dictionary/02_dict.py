mb1 = {"kim":33, "park":44, "choi":55}
mb2 = {"kim":77, "jung":88, "hong":99}

print(mb1['park'])
print(mb1.get('lee')) # 없으면 none

if mb1.get('jung') == None:
    print('jung 없음')
else:
    print('jung 있음')

mb1.update(mb2)
print(mb1)

mb1.clear()
print(mb1)
