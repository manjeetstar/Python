x="Manjeet"
print(f"Name of the candidate is {x}",x, sep=" :::", end="\n")

a, b=map(int, input("Enter two number :").split(" "))
print("Addition is ", a+b)

print(2 + 3 * 4 ** 2)

def findEven(n):
    return n if n%2 == 0 else None


a=[3,4,5,6,7]
b=list(filter(findEven, a))
print(b)