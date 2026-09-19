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

ages=[10,3,45,32,24]
result=reduce(lambda a, b: a+b, list(map(lambda y: y*2, filter(lambda x: x%2 == 0, ages))), 0)
print(result)