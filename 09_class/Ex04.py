class Service:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

if __name__ == '__main__':
    s1 = Service('웬디')
    s1.show()
