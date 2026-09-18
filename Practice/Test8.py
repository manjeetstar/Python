class Manager:
    def __new__(cls, name, age):
        print("Object created")
        return super().__new__(cls)
    
    def __init__(self, name, age):
        print("Initialization Done")        
        self.name=name
        self.age=age        

    def __str__(self):
        return (f"Manager name and age is {self.name} and {self.age}")

    def __repr__(self):
        return (f"Developer debugging : {self.name} {self.age}")

    def __add__(self, other):
        return self.age + other.age

    def __eq__(self, other):
        return self.age == other.age

m1=Manager("Manjeet", 20)
m2=Manager("Awatar", 20)
print("sum of 2 ages is ", m1 + m2)
print(m1 == m2)