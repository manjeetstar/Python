from functools import reduce, wraps
def repeat(n):
    def decoratorF(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Wrapper Execution started -{func.__name__} {args}")
            ctr=[x**2 if isinstance(x, (int, float)) else x for x in args]
            ctr1={k:v.upper() if isinstance(v, str) else v for k,v in kwargs.items()}
            print("Updated arguments is ", ctr)
            result=None
            for _ in range(n):
                result=func(*ctr, **ctr1)
                print("Iteration result:", result)
            return result
        return wrapper
    return decoratorF

@repeat(5)
def display(a,b,**c):
    print(f"This is the main function")  
    print(f"Name of the candidate is {c.get('name')}")
    return a+b 

print(display(5, 10, name="Manjeet"))
print(display.__name__)