from functools import reduce
ctr=[
    ("Manjeet",20),
    ("Awatar", 30),
    ("Parul", 4)
]

value= min(ctr, key=lambda x:x[1])
print(value)