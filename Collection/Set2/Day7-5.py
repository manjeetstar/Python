class A:
    def show(self):
        print("Show method of class A")

class B:
    def show(self):
        print("Show method of class B")

class C(A,B):
    def show(self):
        super().show()
        print("Show method of class C")

print(C.mro())
ctr=C()
ctr.show()