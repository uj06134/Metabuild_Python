import xml.etree.ElementTree as ET
tree = ET.parse('file/Car_Info.xml')
myroot = tree.getroot()

for car in myroot.iter('car'):
    one_car = []
    name = car.find('brand').attrib['name']
    one_car.append("브랜드: " + car.find('brand').text + f"({name})")
    one_car.append("모델:" + car.find('model').text)
    one_car.append("제조년도:" + car.find('year').text)
    one_car.append("색상:" + car.find('color').text)

    print(one_car)


