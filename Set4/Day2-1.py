class Employee:
    country="Canada"
    __dob="930202"

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name and age of candidate is {self.name} and {self.age}")

    @classmethod
    def displayOrigin(cls):
        print(f"Candidate belongs to {cls.country}")

    @staticmethod
    def calculate(a, b):
        print(f"Sum of two numbers is {a+b}")

e1=Employee("Manjeet", 20)
e2=Employee("Parul", 19)
e1.display()
e2.display()
e1.displayOrigin()
e2.displayOrigin()
e1.calculate(5,10)
print(e1._Employee__dob)