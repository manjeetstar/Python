def age():
   a=(x for x in range(10))
   print(type(a))
   for value in a:
      yield value

for x in age():
   print(x)

def display(filename):
   with open(filename) as file:
      for line in file:
         yield line

g=display("../test.txt")
print(next(g))
print(next(g))
print(next(g))

def calculate():
   status=0
   while True:
      value=yield status
      status=status+value

g5=calculate()
next(g5)
print("Checking send value to generator", g5.send(20))
print("Checking send value to generator", g5.send(30))