from bs4 import BeautifulSoup
with open("example.html", "r") as fp:
    soup = BeautifulSoup(fp, "html.parser")

print("1:", soup.title)
print("2:", soup.title.name)
print("3:", soup.title.string)
print("4:", soup.title.parent)
print("5:", soup.title.parent.name)
print("6:", soup.p)
print("7:", soup.div)
print("8:", soup.table)
print("9:", soup.find_all('div'))
print("10:", soup.find_all('p'))
print("11:", soup.find_all('div','ex_class'))
print("12:", soup.find_all(id='ex_id'))
print("13:", soup.find_all('div', id='ex_id'))