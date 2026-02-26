import os, signal
from MyPackage.emicalculate import calculate

class calculateException(Exception):
    def __init__(self, message):
        super().__init__(f"Issue occured: {message}")
        self.message=message


def calculate1():
    a = 10
    try:
        if a <= 10:
            raise calculateException("Issue Occured")
    except calculateException as e:
        print("Exception handled with message-", e.message)
    finally:
        print("finally block will be executed")

calculate1()

calculate()

print(os.getcwd())

try:
    with open("../test.txt", "a") as f:
        f.write("This is just to see whether it takes correct file path or not")
except FileNotFoundError as e:
    print("No such file exists")
finally:
    print("This block will be executed")
