def calculate(a:int, b:int) -> int :
    try:
        c=a+b
        return c
    except TypeError:
        print("Seems like some abronmal type being passed")
    finally:
        print("This will be executed always")

ctr= calculate(5,"10")
print(f"Sum is {ctr}")