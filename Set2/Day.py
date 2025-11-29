def Method1(a):
    def closureMethod1(b):
        return a*b
    
    return closureMethod1

a=Method1(3)
print(a(2))

def Method2(a, b):
    return a+b, a-b, a*b

print(Method2(10,2))