class Employee:
    country="Canada"
    __dob="930202"

    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.__gender=gender

    def display(self):
        print(f"Name and age of candidate is {self.name} and {self.age}")

    @classmethod
    def displayOrigin(cls):
        print(f"Candidate belongs to {cls.country}")

    @staticmethod
    def calculate(a, b):
        print(f"Sum of two numbers is {a+b}")

e1=Employee("Manjeet", 20,"Male")
e1.display()
e1.displayOrigin()
print(e1.__dict__)
