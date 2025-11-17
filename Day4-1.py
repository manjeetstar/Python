class Employee:
    _name="Manjeet"

    def __init__(self, age, address):
        self.age=age
        self.address=address

    def display(self):
        print(f"Name of candidate is {self._name} who is {self.age} years old from {self.address}")

    @classmethod
    def displayDetails(cls):
        print(f"Name of the canidate is {cls._name}")

    @staticmethod
    def calculate(a,b):
        return a+b
        

p1=Employee(20, "Canada")
p1.display()
Employee.displayDetails()
print("Sum of two numbers is ", Employee.calculate(2,3))