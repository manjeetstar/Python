from abc import ABC, abstractmethod

class Employee(ABC):
    empDept="Operations"

    def __init__(self, Name, Age, phoneno):
        self.empName=Name
        self.empAge=Age
        self.__phoneno=phoneno

    @property
    def phoneno(self):
        return self.__phoneno

    @phoneno.setter
    def phoneno(self, phone):
        self.__phoneno=phone

    def display(self):
        print(f"Name and age of the employee is {self.empName} & {self.empAge}")

    @classmethod
    def calculate(cls):
        print(f"Name of the department is {cls.empDept}")

    @staticmethod
    def utility(a,b):
        return a*b

    @abstractmethod
    def absfunction(self):
        pass

class Employee1(Employee):
    def __init__(self, name, age, phone):
        super().__init__(name, age, phone)
        self.name=name
        self.age=age
        self.phone=phone

    def absfunction(self):
        print("This is the abstract method implemented in the subclass by ", self.name)

emp=Employee1("Manjeet",20, 214)
emp.display()
Employee1.calculate()
print(f"Displaying instance variables value is {emp.empName} and {emp.empAge}")
print("Output of utility function is ", Employee.utility(5,12))
emp.absfunction()
emp.phoneno="9899769493"
print("Phone number is ", emp.phoneno)
print(emp._Employee__phoneno)
        