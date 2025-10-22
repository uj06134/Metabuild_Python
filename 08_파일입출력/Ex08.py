import xml.etree.ElementTree as ET
# xml 파일 읽기1
# with open('student.xml', 'r', encoding='utf-8') as f:
#     xmlData = f.read()
#     # print(xmlData)
#
# myroot = ET.fromstring(xmlData)

# xml 파일 읽기2
tree = ET.parse('file/student.xml')
myroot = tree.getroot()

totalList = []
for stu in myroot.iter('student'):
    # print(stu)
    onePerson = []
    onePerson.append(stu.find('name').text)
    onePerson.append(stu.find('국어').text)
    onePerson.append(stu.find('영어').text)
    onePerson.append(stu.find('수학').text)

    # 합계 추가
    total_score = int(stu.find("국어").text) + int(stu.find("영어").text) + int(stu.find("수학").text)
    onePerson.append(total_score)
    totalList.append(onePerson)
print(totalList)
