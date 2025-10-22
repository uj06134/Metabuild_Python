import json
d = {'name':'아이유', 'age':40, 'addrss':{'city':'서울', 'gu':'종로구'}}
print(d['name'])
print(d['age'])
print(d['addrss']['city'])
print(d['addrss']['gu'])

fr = open('file/jumsu.json', 'r', encoding='utf-8')
readString = fr.read()
print(readString)
print(type(readString))
fr.close()

json_data = json.loads(readString)
print(json_data)
print(type(json_data))

totalList = []
for person in json_data:
    total_score = int(float(person['kor']) + float(person['eng']) + float(person['math']))
    gender = "남자"
    if person['gender'] == 'F':
        gender = "여자"
    t = (
        person['name'],
        person['kor'],
        person['eng'],
        person['math'],
        total_score,
        gender
    )
    totalList.append(t)
print(totalList)