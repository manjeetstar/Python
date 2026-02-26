class DieselEngine:
    def __init__(self):
        print("Constructor of Class A")
    def start(self):
        print("Started diesel engine")
    def Stop(self):
        print("Stopped disel engine")

class PetrolEngine:
    def __init__(self):
        print("Constructor of Class A")
    def start(self):
        print("Started Petrol engine")
    def Stop(self):
        print("Stopped Petrol engine")

class Car:
    def __init__(self):
        self.d1=DieselEngine()
        self.p1=PetrolEngine()

    def drive(self):
        self.p1.start()
        print("Driving Car")
        self.p1.Stop()

c=Car()
c.drive()
