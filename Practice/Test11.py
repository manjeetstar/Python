from dataclasses import dataclass, field
from typing import ClassVar

@dataclass(frozen=False, order=True)
class Manjeet:
    name: str        
    age: ClassVar[int] = 20
    address: dict = field(default_factory=dict, compare=False)

m1=Manjeet("Manjeet")
m2=Manjeet("Manjeet")
m1.address["addressLine1"]="Essex Squaer 23"
m1.name="Parul"

print(m1, m1.age)
print(m2, m2.age)
print(m1 == m2)