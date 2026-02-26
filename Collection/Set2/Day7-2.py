class Student:
    __name="Parul"
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value

class Student1:
    __name="Parul"

    def __init__(self, age, gender, **kwargs):
        super().__init__(**kwargs)
        self.age=age
        self.gender=gender
    
    def display(self):
        print(f"Age and gender of candidate is {self.age} and {self.gender}")
        
class Student2:  
    def __init__(self, address, zipcode, **kwargs):
        super().__init__(**kwargs)
        self.address=address
        self.zipcode=zipcode

    def display(self):
        print(f"Address and zipcode of candidate is {self.address} and {self.zipcode}")

class Class(Student1, Student2):
    def __init__(self, age, gender, address, zipcode):
        super().__init__(age=age, gender=gender, address=address, zipcode=zipcode)
        
    def show(self):
        print(self._Student1__name)

c1=Class(20, "Male", "Canada", 8228)
c1.show()
c1.display()
Student2.display(c1)