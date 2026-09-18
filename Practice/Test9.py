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