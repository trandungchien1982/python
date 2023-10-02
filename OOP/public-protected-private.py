from datetime import datetime

print('Các ví dụ liên quan đến public/protected/private variable/methods ...')
print('----------------------------------------------------------------------------')


class Person:
    # public
    name: str
    age: int

    # protected
    _birthday: datetime

    # private
    __active: bool

    # Hàm tạo mặc định + customize
    def __init__(self, newName: str = 'EMPTY', newAge: int = 10, newBirthday: datetime = datetime(2020, 10, 10)):
        self.name = newName
        self.age = newAge
        self._birthday = newBirthday
        self.__active = True

    def __del__(self):
        print('--------------------------------------------')
        print('Tiến hành gọi hàm destrutor() của Person ...' + self.name)
        print('------------- END --------------------------')

    def setName(self, newName: str):
        self.name = newName

    def setAge(self, newAge: int):
        self.age = newAge

    def showAllData(self):
        print('------> name: ' + self.name
              + ', age: ' + str(self.age)
              + ', birthday: ' + str(self._birthday)
              + ', active: ' + str(self.__active)
              )


p = Person()
print('\n----------------- Show Person (new created) ----------------')
print('   ------> ' + str(p))

p.__setattr__('attr02', 'Value 02222222222')
p.__setattr__('attr03', 'Giá trị của Attribute 03')

print('Value of attr02: ' + p.attr02)
print('Value of attr03: ' + p.attr03)
p.showAllData()
