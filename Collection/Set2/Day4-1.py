a=[4,5,6,7]
names=["manjeet", "sanjeet", "Parul"]
ctr=list(map(lambda x: x**2, a))
print(ctr)

ctr1=list(filter(lambda x: len(x)<7, names))
print(ctr1)

d={"a":4, "b":8, "c":2, "d":3}
print(d.items())
ctr2=sorted(d.items(), key=lambda x:x[1])
print(ctr2)


for i in range(3):
    print(i)