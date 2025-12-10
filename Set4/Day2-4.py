from abc import ABC, abstractmethod

class A(ABC):
    __name="Manjeet"
    _age=20

    def __init__(self):
        super().__init__()
        print("Constructor present in abstract class")

    @abstractmethod
    def display():
        pass

    @classmethod
    def personal(cls):
        print(f"Name and age of the candidate is {cls.__name} and {cls._age}")

    def display1(self):
        print("This is display1 method")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of class B")

    def display(self):
        print("implemented abstract method")

b1=B()
b1.display()
b1.display1()
print(b1._age, b1._A__name)
b1.personal()
