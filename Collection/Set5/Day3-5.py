def outer():
    x=2
    def inner():
        nonlocal x
        x=x+1
        print(x)
    return inner

d=outer()
print(outer.__dict__)