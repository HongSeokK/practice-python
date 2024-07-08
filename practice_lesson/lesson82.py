class Car(object):
    def __init__(self, model = None):
        self.model = model
    def run(self):
        print('run')
#        print('run {}'.format(self.__class__.__name__))

class ToyotaCar(Car):
    def run(self):
        # 親の init 呼び出し、そのあとに新規処理を入港
        super().run()
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # 親の init 呼び出し
        super().__init__(model)
        self.enable_auto_run=enable_auto_run
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyota_car = ToyotaCar('Lexus')
toyota_car.run()
print(toyota_car.model)

tesla_car = TeslaCar()
print(tesla_car.model)
tesla_car.auto_run()
tesla_car.run()