a=[1,2,3,4,5,2,3,4,4]
b=[3,4,5,6]
c=[]

for ctr in a:
    if ctr not in b:
        c.append(ctr)

print(c)

a=[x*x for x in range(2,20,2)]
print(a)