a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

op=str(input("Enter the operation:"))

if op == "+":
    print(f"Sum of two number is {a+b}")
elif op == "-":
    print(f"Difference of two number is {a-b}")
elif op == "*":
    print("Product of two number is ", type(str(a*b)))
else:
    print("No operation needed by the user")