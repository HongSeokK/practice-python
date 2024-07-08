class Car(object):
    def __init__(self, model = None):
        self.model = model
    def run(self):
        print('run')
class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        # 親の init 呼び出し
        super().__init__(model)
        # __ の場合は外からは参照できなくなる
        # setter / getter property でのみ間接可能
        self.__enable_auto_run=enable_auto_run
        self.passwd=passwd

    # Getter
    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    # Setter
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd=='456':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')
    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar(passwd='456')
tesla_car.run()
#print(tesla_car.enable_auto_run)
