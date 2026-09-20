from typing import Literal, TypedDict

def calculate(a:int,b:int)->None:
    c:int=a+b 
    print(f"Sum of two numbers is {a+b}", c)

calculate(5,10)

employee: dict[str, str | int | bool] ={
    "name":"Manjeet",
    "age": 20,
    "address" : False
}

print(employee)

ctr:list[int, bool, str] = [20, True, "Manjeet"] # type: ignore
print(ctr)

class Manager(TypedDict):
    name: Literal["Manjeet"]
    age: int
    address: str
    Married: bool | None
    status: Literal["pending", "success", "failed"]

m1:Manager={
    "name": "Manjeet",
    "age": 20,
    "address": "Canada",
    "Married": True, 
    "status": "success"
}
print(m1)