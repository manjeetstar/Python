# This is Abstration concept related examples
from abc import ABC, abstractmethod
from inspect import isabstract

class candidate(ABC):
    def calc(self):
         print("This is implementation of abstract method") 

    @abstractmethod
    def calculate(self, a, b):
       pass

class candidate1(candidate):
    def calculate(self, a, b):
       print("This is implementation of abstract method")
       return a+b

c1=candidate1()
print(c1.calculate(3,4))
c1.calc()
print(isabstract(candidate))
print(candidate1.mro())
