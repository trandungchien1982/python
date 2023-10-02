from abc import ABC, abstractmethod

print('Các ví dụ liên quan đến Abstraction ...')
print('--------------------------------------------')


# Person là 1 abstraction class
class Person(ABC):
    name: str
    age: int

    # Hàm tạo mặc định + customize
    def __init__(self, newName: str = 'EMPTY', newAge: int = 10):
        self.name = newName
        self.age = newAge

    def setName(self, newName: str):
        self.name = newName

    def setAge(self, newAge: int):
        self.age = newAge

    def showAllData(self):
        print('------> name: ' + self.name
              + ', age: ' + str(self.age)
              )

    @abstractmethod
    def methodAbstract01(self):
        print('----------------------------------------------------')
        print('---- Method Abstract01, name: ' + self.name)
        print('---- Method Abstract01, age: ' + str(self.age))

    @abstractmethod
    def methodAbstract02(self):
        print('----------------------------------------------------')
        print('---- Method Abstract02, name: ' + self.name)
        print('---- Method Abstract02, age: ' + str(self.age))


try:
    print('Try to initialize Person ...')
    person = Person()
    print('After init Person ...')
except Exception as ex:
    print('Exception occur: ... [' + str(ex) + ']')


# Real implementation of class Person
class RealPerson(Person):
    def methodAbstract01(self):
        print('\n------ RealPerson.methodAbstract01: ')
        super().methodAbstract01()

    def methodAbstract02(self):
        print('\n------ RealPerson.methodAbstract02: ')
        super().methodAbstract02()


print('\n------------------------------------------------------------------------')
realPerson = RealPerson()
realPerson.methodAbstract01()
realPerson.methodAbstract02()
print('--------------- Ket thuc RealPerson ------------------')
