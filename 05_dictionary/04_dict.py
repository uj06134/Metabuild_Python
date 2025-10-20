person = {
    'kim':{"나이":20, "주소":"서울"},
    'hong':{"나이":30, "주소":"부산"},
}
for k,v in person.items():
    print(k)
    for i,j in v.items():
        print(i,j)