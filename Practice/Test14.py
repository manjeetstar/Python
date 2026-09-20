
def logicDecorator(func):
    def wrapper(*args, **kwargs ):
        print("This is start of the logger utility")
        result=func(*args, **kwargs)
        print("Sum of two numbers is ", result)
        print("This is end of the logger utility")
        return result
    return wrapper

@logicDecorator
def calculate(a, b):
    return a+b    

calculate(10,20)