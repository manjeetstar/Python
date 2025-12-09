class A:
    def display(self):
        print("This is display method of class A")
        return 1

class B:
    def display(self):
        print("This is display method of class B")
        return 2

class C(A,B):
    pass

c1=C()
print(c1.display())
print(C.__mro__)