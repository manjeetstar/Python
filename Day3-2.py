try:
    with open("test1.txt", "r+") as f:
        f.write("\nAt the end of file")
        f.seek(0)
        print(f.read())
        print(f.__getattribute__("mode"))
except FileNotFoundError as e :
    print(f"Error: This is due to file doesnt exist", e)
except BufferError as b:
    print(f"Error is {b}")