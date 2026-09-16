
def calculate():
    a,b=10,0
    try:
        raise TypeError("This is type error")
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
        return 5
    else:
        print("This is else block")
        return 6
    finally:
        print("This is finally block for cleanr up activitiy")

print(calculate())
        