def calculate(value):
    str="This is Manjeet"
    ctr=0
    ctr1=10
    def inner():
        nonlocal ctr, ctr1
        print("Accessing outside variable - ", value, str)
        ctr=ctr+1
        ctr1=ctr1+1
        return ctr, ctr1
    return inner

value=calculate("Main")
print(value())
print("Closure informations", value.__closure__[1].cell_contents)

def factory():
    str=[]
    for i in range(3):
        def innerfunction(i=i):
            return i

        str.append(innerfunction)
    return str

fact=factory()
for factt in fact:
    print(factt())
