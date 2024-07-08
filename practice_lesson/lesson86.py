import abc

# abstract, 抽象クラス
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # 必ず継承して実装する必要があるとのあかし
    @abc.abstractmethod
    def drive(self):
        pass
class Baby(Person):
    def __init__(self,age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception("can't drive")

class Adult(Person):
    def __init__(self,age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print('ok')

class Car(object):
    def __init__(self, model = None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

baby = Baby()
adult = Adult()
car = Car()
car.ride(adult)
