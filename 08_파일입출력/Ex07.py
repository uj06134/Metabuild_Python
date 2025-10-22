import json
from datetime import datetime

fr = open('file/humans.json', 'r', encoding='utf-8')
readString = fr.read()
fr.close()
json_data = json.loads(readString)
totalList = []
for person in json_data:
    year = person['ssn'].split('-')[0][:2]
    now_year = datetime.now().year
    if int(year) >= 50:
        year = "19" + year
    else:
        year = "20" + year
    age = now_year - int(year)

    gen_num = int(person['ssn'].split('-')[1][0])
    gender = ''
    if (gen_num == 1) or (gen_num == 3):
        gender = "남자"
    elif (gen_num == 2) or (gen_num == 4):
        gender = "여자"

    t = (
        person['name'],
        age,
        person['address'],
        person['hobby'],
        person['ssn'],
        gender
    )
    totalList.append(t)
print(totalList)
