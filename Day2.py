a, b, c = 100, 20, 0
print(f"The two numbers are {a+b} and {a-b} and {a*b} and {a/b} and {a**b}")
print(a>b and b<a)

name = ["Manjeet", "Sanjeet", "Parul", "Awatar"]
print("Manjeet" in name)

if a>b and a>c:
    print(f"Value of a is {a}")
else:
    print("No it is not greatest number")

for i in ["manjeet", "sanjeet","Rahul"]:
    print(i, end=" ")
    print()

while b<100:
    print(b, end=" ")
    b=b+1
else:
    print()
    print("Loop executed successfully")

for i in range(1,7):
    for j in range(1, i):
        print("*", end=" ")
    print()


    