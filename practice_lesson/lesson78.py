class Person(object):
    def __init__(self, name='default'):
        self.name = name
        print(self.name)
    def say_something(self):
        print('I am {0}. Hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('good bye')


person2 = Person('mike')
person2.say_something()
del person2
#del(person2)

print('@@@@@@@@@@@@@@@@@@@@')
# person.say_something()