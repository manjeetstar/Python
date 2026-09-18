class Manager:
    salary=[100,200,300]

    def __new__(cls, name, age):
        print("Object created")
        return super().__new__(cls)
    
    def __init__(self, name, age):
        print("Initialization Done")        
        self.name=name
        self.age=age
        self.salary=[10,20,30]
        self.index=0        

    def __str__(self):
        return (f"Manager name and age is {self.name} and {self.age}")

    def __repr__(self):
        return (f"Developer debugging : {self.name} {self.age}")

    def __add__(self, other):
        return self.age + other.age

    def __eq__(self, other):
        return self.age == other.age

    def __call__(self):
        print("This is turning object into callable")

    def __bool__(self):
        return bool(self.name)

    def __getitem__(self, key):
        return (f"Returned name is {self[key]}")

    def __setitem__(self, key, value):
        self[key]=value

    def __contains__(self, item):
        return item in self.name

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.salary):
            raise StopIteration
        value=self.salary[self.index]
        self.index += 1
        return value

m1=Manager("Manjeet", 20)
m2=Manager("Awatar", 20)
print("sum of 2 ages is ", m1 + m2)
print(m1 == m2)
m1()
print(bool(m1), m1.name)
m1.name="Manjeet Singh"
print("Updated name is ", m1.name)
print("Manjeet Singh" in m1)

for item in m1:
    print(item)