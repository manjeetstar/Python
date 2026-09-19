from functools import reduce
ctr=[
    ("Manjeet",20),
    ("Awatar", 30),
    ("Parul", 4)
]

value= min(ctr, key=lambda x:x[1])
print(value)

result=(lambda x: x*2)(10)
print(result)

def calculate(x):
    return lambda y: y*x

result=calculate(5)
print(type(result))
print(result(20))