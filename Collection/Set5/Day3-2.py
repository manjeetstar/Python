from functools import wraps
def A(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator A Started")
        print("Decorator A Started")
        func()
    return wrapper

def B(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator B Started")
        print("Decorator B Started")
        func()
    return wrapper


@B
@A
def display():
    print("This is the main method which will be decorated")

display()
