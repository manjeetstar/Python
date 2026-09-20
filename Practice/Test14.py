import time
from functools import wraps

def retry(times):
    def logicDecorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs ):  
            for ctr in range(1, times+1):
                print(f"Calling {func.__name__} utility , Attempt- {ctr}")
                start=time.perf_counter()
                result=func(*args, **kwargs)
                print("Sum of two numbers is ", result)
                end=time.perf_counter()
                print("Sum of two numbers is ", result)
                print(f"Finished {func.__name__} utility")
                print(f"Total time taken by the function : {end - start:.9f} seconds")                
        return wrapper
    return logicDecorator

@retry(times=2)
def calculate(a, b):
    return a+b    

calculate(10,20)
