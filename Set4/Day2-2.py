class Employee:
    __name="Manjeet"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name=value

    def __calculate(self, a, b):
        return a+b

class Employee1(Employee):
    pass

E2=Employee1()
print(E2._Employee__calculate(5,10))
