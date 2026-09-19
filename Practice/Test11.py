from dataclasses import dataclass

@dataclass
class Manjeet:
    name: str
    age: int
    address: dict

m1=Manjeet("Manjeet",20, {"addressLine1": "Sussex 3B", "zipcode": 203, "city": "Vancouver"})

print(repr(m1))