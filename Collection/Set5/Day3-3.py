class clbDecorator:
    def __init__(self, func):
        self.func=func

    def __call__(self):
        print(f"Class based decorator has been called")
        result=self.func()
        print(f"Return result is ", result)
        print("Class based decorator has been finished")

@clbDecorator
def display():
    print("This is to display display function")
    return 5

display()
print(clbDecorator.__dict__.items())