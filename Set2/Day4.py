"""
This is an example of Decorator function 
"""
def AddLogic(func):
    def wrapper(*args, **kwargs):
        print("This is the start of wrapper login")
        c=func(*args)
        print("This is the end of the logic")
        return c

    return wrapper


@AddLogic
def calculate(a:int, b:int)->int:
    return a+b

print(calculate(5,6))