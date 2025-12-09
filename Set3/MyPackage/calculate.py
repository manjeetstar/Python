

def add(a,b):
    print(f"Addition of two numbers {a} {b} is {a+b}")

def substract(a,b):
    result=(b-a) if b>a else (a-b)
    return result

def main():
    add(2,5)
    substract(15,20)

if __name__ == "__main__":
    print("Executing without __name__==__main__ block")
    main()