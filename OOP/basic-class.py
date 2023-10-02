import string
from datetime import datetime

print('Các ví dụ liên quan đến Class cơ bản (member/constructor/destructor ...')
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


def showData(p: Person):
    print(' ---> Hiển thị data của person: ' + str(p))
    p.showAllData()


print(' - Taọ mới class Person ...')
person = Person()
showData(person)
print('---------------------------------')
print('----- Modify data of Person -----')

person.setAge(100)
person.setName('Value of Name')
person.setBirthday(datetime(2022, 7, 8))
person.setActive(False)

print('---------------------------------')
print(' ---- person.age =  ' + str(person.age))
print(' ---- person.name = ' + person.name)

showData(person)

print('---------------------------------')
print('--------- Khởi tạo Person2 ------')
print('---------------------------------')
p2 = Person('NAME 2', 222)
showData(p2)
