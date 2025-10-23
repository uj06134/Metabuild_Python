import re
L = ['ab123', 'cd456', 'xy789', '12ef345qw', 'abc12']
# 정규식 패턴:
# [a-zA-Z]{2} → 알파벳 대소문자 2개
# \d{3}       → 숫자 3개
regex = '[a-zA-Z]{2}\d{3}'

# re.compile()로 정규식을 패턴 객체로 변환
pattern = re.compile(regex)

for item in L:
    # pattern.match() -> 문자열의 패턴이이 정규식과 일치하면 True 반환
    if pattern.match(item):
        print(f"패턴 일치: {item}")
    else:
        print(f"패턴 불일치: {item}")

print("=== match() 결과 ===")
for item in L:
    if re.match(regex, item):
        print(f"패턴 일치: {item}")
    else:
        print(f"패턴 불일치: {item}")
print("=== search() 결과 ===")
for item in L:
    # pattern.search() -> 문자열 전체에서 패턴이 있으면 일치
    if pattern.search(item):
        print(f"패턴 일치: {item}")
    else:
        print(f"패턴 불일치: {item}")

print("------------------------")
L = ['a.txt', 'a12.txt', 'a123.txt', 'a12345.txt']
regex = '[a-z]{1}\d{3,}.txt'

for item in L:
    if re.match(regex, item):
        print(item)
print("------------------------")
L = ['hello!', 'hello안녕~', '하하하', '안녕^^', '반갑습니다.', '또 만나요', '파이썬', 'grape#*']
# + : 앞의 패턴이 '한 글자 이상' 반복됨
# * : 앞의 패턴이 '0번 이상' 반복됨
# ? : 앞의 패턴이 '0번 또는 1번' 나타남
regex = '[ㄱ-힣]+'
result = []
for item in L:
    if re.fullmatch(regex, item):
        print(item)
        result.append(item)

print(result)
print("------------------------")
print(re.findall('[ㄱ-힣]+', '안녕123 하세요!!! hello'))
print(re.sub('\s+','','     안녕     하세요     '))
print("------------------------")
mailList = ['abc@naver.com','xyz@daum.net', 'qwer@gmail.com']
for mail in mailList:
    li =  re.split('@', mail)
    print(f"아이디: {li[0]}" , end=' ')
    print(f"도메인: {li[-1]}")
print("------------------------")
text = '홍길동, 30세'
pattern = re.compile('(.+),\s(\d+)세') # .: 아무 글자
match = pattern.fullmatch(text)
if match:
    print("이름:", match.group(1))
    print("나이:", match.group(2))
print("------------------------")
address = "서울특별시 강남구 역삼동 123-45"
pattern = re.compile('(.+시)\s+(.+구)\s+(.+동)\s+([\d-]+)')
match = pattern.fullmatch(address)
if match:
    print("시:", match.group(1))
    print("구:", match.group(2))
    print("동:", match.group(3))
    print("번지:", match.group(4))
print("------------------------")
text = "오늘은 2025-10-23입니다."
pattern = re.compile('.+\s(\d{4})-(\d+)-(\d+).+')
match = pattern.fullmatch(text)
if match:
    print(f"{match.group(1)}년")
    print(f"{match.group(2)}월")
    print(f"{match.group(3)}일")
print("------------------------")
fr = open("scores.txt", "r", encoding="utf-8")
for line in fr.readlines():
    line = line.strip()
    pattern = re.compile('(.+)\s(\d+)\s(\d+)\s(\d+)')
    match = pattern.fullmatch(line)
    if match:
        total = int(match.group(2)) + int(match.group(3)) + int(match.group(4))
        print(f"{match.group(1)} - {total}" )