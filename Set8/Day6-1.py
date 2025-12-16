from dataclasses import dataclass, field

@dataclass(repr=True)
class employee:
    name:str
    age: int
    isIndian: bool
    country:list[str]=field(default_factory=list, init=False)

    def __post_init__(self):
        if self.name == "Manjeet":
            raise ValueError("Error in name constraint")


e1=employee("Manjeet2", 20, False)
e2=employee("Manjeet1", 20, False)
e1.country.append("US")
print(e2)
