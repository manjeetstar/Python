class Day1:
    def method(self):
        print("This is Day1 method")

class Day2(Day1):
    def method(self):
        print("This is Day2 method")

d=Day1()
Day2.method(d)