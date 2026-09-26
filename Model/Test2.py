def calculate():
    str="This is Manjeet"
    ctr=0
    def inner():
        nonlocal ctr
        print("Accessing outside variable - ", str)
        ctr=ctr+1
        return ctr
    return inner

value=calculate()
print(value())
print(value())
print(value())