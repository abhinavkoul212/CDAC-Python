from abc import ABC,abstractmethod

class Animal(ABC):
    #concrette methods are allowed in abstract class
    @abstractmethod
    def hello(self):
        pass

    @staticmethod
    def test():
        print("Testing.............")

    def printable(self):
        print("Printtable")

class Cat(Animal):
    def hello(self):
        print("Helo from cat")

#ani=Animal()   nai banega object kyunki wo abstract le liya hai
ca= Cat()
ca.hello()

#ca.test()
Animal.test()
#Animal.printable()
ca.printable()

