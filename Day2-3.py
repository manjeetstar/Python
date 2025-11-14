def validate(a, b, *args, **kwargs):
    print(f"This is first program - {a} and {b}")
    value=[x*2 for x in args if type(x) is not str]
    print(f"Value of tuple stuff is {value}")
    return args, kwargs
    
t1=()
t2={}
t1, t2= validate(10,20, "Manjeet", 7, 20, name="Manjeet", age=20, address="Canada")
print(f"return value is {t1} and {t2}")