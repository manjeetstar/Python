def calculate(*args, **kwargs):
   """ This method is being used for calculating unknown arguments and keyword arguments"""
   total=0
   for i in args:
      total=total+i  
   print(f"Employee with name {kwargs["name"]} resides at {kwargs["address"]} ")    
   return total

print("Total is ", calculate(10,20,30, name="Manjeet", address="Canada"))
print(calculate.__doc__)

square=lambda x: x*x
print(square(19))