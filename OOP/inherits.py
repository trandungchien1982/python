import string
from datetime import datetime

print('Các ví dụ liên quan đến kế thừa Class ...')
print('--------------------------------------------')


class Person:
    name: str
    age: int
    birthday: datetime
    active: bool

    # Hàm tạo mặc định + customize
    def __init__(self, newName: str = 'EMPTY', newAge: int = 10, newBirthday: datetime = datetime(2020, 10, 10)):
        self.name = newName
        self.age = newAge
        self.birthday = newBirthday
        self.active = True

    def __del__(self):
        print('--------------------------------------------')
        print('Tiến hành gọi hàm destrutor() của Person ...' + self.name)
        print('------------- END --------------------------')

    def setName(self, newName: str):
        self.name = newName

    def setAge(self, newAge: int):
        self.age = newAge

    def increaseAge(self, units: int):
        self.age += units

    def setBirthday(self, newBd: datetime):
        self.birthday = newBd

    def setActive(self, newActive: bool):
        self.active = newActive

    def showAllData(self):
        print('------> name: ' + self.name
              + ', age: ' + str(self.age)
              + ', birthday: ' + str(self.birthday)
              + ', active: ' + str(self.active)
              )


class Animal:
    def eat(self):
        print('Animal: eat() ...')

    def sleep(self):
        print('Animal: sleep() ...')

    def doNothing(self):
        pass


class Male(Person, Animal):
    def __init__(self):
        super().__init__()
        self.age = 1234
        self.name = 'Name of MALE'

    def increaseDoubleAge(self, doubleAgeVal: int):
        self.age = pow(super().age, 2)

    def toString(self):
        return 'All string data of : ' + str(self)


male = Male()
print('\n----------------- Show all data of Male after being created -----------')
male.showAllData()

print('\n----------------- Try to update some properties of Male ---------------')
male.age = 12
male.name = 'Update Name of MALE'
male.active = False

male.eat()
male.sleep()
male.doNothing()

male.showAllData()

print('\n------------------------------------------------------------------------')


class Female(Person, Animal):
    def showFemaleData(self):
        super().eat()
        super().sleep()
        super().doNothing()
        print('--- Show Female name: ' + self.name)
        print('--- Show Female age: ' + str(self.age))


female = Female()
female.name = 'Name of MALE'
print('\nData of Female --------------------------------------')
print('Person: ' + female.name)
print('Person: ' + str(female.age))
female.showFemaleData()
