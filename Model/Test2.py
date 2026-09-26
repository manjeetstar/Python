def calculate():
    str="This is Manjeet"
    ctr=0
    ctr1=10
    def inner():
        nonlocal ctr, ctr1
        print("Accessing outside variable - ", str)
        ctr=ctr+1
        ctr1=ctr1+1
        return ctr, ctr1
    return inner

value=calculate()
print(value())
print(value())
print(value())

print("Closure informations", value.__closure__[1].cell_contents)