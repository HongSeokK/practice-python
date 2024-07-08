class Car(object):
    def run(self):
        print('run')
#        print('run {}'.format(self.__class__.__name__))

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.auto_run()
tesla_car.run()