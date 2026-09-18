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
   status, ctr =0, 0
  
   for ctr in range(5):      
        value=yield status
        status=status+value  

g5=calculate()
try:
    print(next(g5))
    print("Checking send value to generator", g5.send(20))
    print("Checking send value to generator", g5.send(30))
    print("Checking send value to generator", g5.send(30))
    print("Checking send value to generator", g5.send(30))
    print("Checking send value to generator", g5.send(30))
except StopIteration as e:
   print("Generator has finished")
finally:
   print("Rest of the code...")