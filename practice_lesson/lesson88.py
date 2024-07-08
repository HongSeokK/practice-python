class Person(object):
    __kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name,self.__kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()


class T(object):

    # 違う客体でも共有されてしまうので注意する必要がある
    # words = []

    def __init__(self):
        self.words = []

    def add_word(self,word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 3')
print(c.words)

d = T()
d.add_word('add 2')
d.add_word('add 4')
print(c.words)
print(d.words)