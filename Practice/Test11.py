from dataclasses import dataclass, field, fields
from typing import ClassVar

@dataclass(frozen=False, order=True)
class Manjeet:
    name: str        
    age: int = 20
    address: dict = field(default_factory=dict, compare=False)

    def display(self):
        print("This is display method defined in the dataclass", self.name, self.age, self.address)

m1=Manjeet("Manjeet")
m2=Manjeet("Manjeet")
m1.address["addressLine1"]="Essex Squaer 23"
m1.name="Parul"

print(m1, m1.age)
print(m2, m2.age)
print(m1 == m2)
m1.display()

for c1 in fields(m1):
    print(c1.name, c1.type)