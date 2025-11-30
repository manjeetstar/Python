class Employee:
    country="Canada" # Class attributes

    def __init__(self, name, age, gender):
        self.name, self.age, self.gender=name, age, gender # Instance attributes

    def calculate(self):
        print(f"Name of the candidate is {self.name}")

    @classmethod
    def origin(cls):
        print(f"Candidate belongs to {cls.country}")

    @staticmethod
    def display():
        print("This is a utility function")
    

e1=Employee("Manjeet", 20, "Male")
e2=Employee("Parul", 120, "Female")

e1.calculate()
e1.origin()
e1.display()

print(f"Instance dict items are {e1.__dict__}")
print(f"Class dict items are {Employee.__dict__}")        