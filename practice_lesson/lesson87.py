class Person(object):
    def talk(self):
        print('talk')
    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('run')

# 多重継承を行ったときは、左にくるクラスの関数を優先する
class PersonCarRobot(Car,Person):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()