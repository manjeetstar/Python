from contextlib import contextmanager

class CManager:
    def __enter__(self):
        print("Acquiring the resources")
        return "Manjeet Singh"

    def __exit__(self, exc_type, exc, tb):
        print("Cleaning up the resources")
        return True

with CManager() as m:
    print("Main Context Manager code")
    print(f"Returned context is {m}")
    raise ValueError("This is exception")

print("Rest of the code...")

@contextmanager
def dbManagement():   
    
    try: 
        yield "Manjeet", "Singh"
    finally:    
        print("Performed cleanup activities")

with dbManagement() as (a, b):
    print(f"Returned outcomes {a} {b}")
    raise ValueError("This is the error")