def add():
    """
    This method is being used for calculating sum of two numbers
    """
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    z= x+y
    print(f" Both the numbers are {x} and {y} and their sum is {z}")

x, y, z=1000, 20, 20

add()
print(add.__doc__, " ", type(x))
print(f"Memory reference of x and y is {id(x)} and {id(z)}")

print(float("45.6"))