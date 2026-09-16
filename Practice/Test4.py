
print("This is at the top of the module")

def calculate(*args, **kwargs):
   """ This method is being used for calculating unknown arguments and keyword arguments"""
   total=0
   for i in args:
      total=total+i  
   print(f"Employee with name {kwargs["name"]} resides at {kwargs["address"]} ")    
   return total

# print("Total is ", calculate(10,20,30, name="Manjeet", address="Canada"))

def display(a,b,c,d):
   print("The values are ", a,b,c,d)

a={
   "a":10,
   "b":20,
   "c":30,
   "d":40
}
# display(**a)

d=10
e=[1,2,3,4]
def display(d,y):
   d=d+1
   y.append(15)

   return d, y

# print(display(d,e))

print("Golbal namespace are ", globals()["e"])

y=20
def function1():
    x=10
    def function2():
       global y
       y=30
       nonlocal x
       x=20
       print(x, y)
    function2()
    print(x, y)

# function1()

def function2(x,y):
   return x+y

if __name__ =="__main__":
   print(f"Sum is {function2(5,11)}")
