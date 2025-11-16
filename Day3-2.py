import json
import os
from pathlib import Path
from MyPackage import add, minus
from MyPackage.SubPkg import calculate

address={
    "addressline1": "Canada",
    "addressline2": "Valcouver",
    "zipcode": 20202,
    4: "Manjeet Singh",
    "famous": [1,32,4,5,3,65]
}

with open("test1.json", "w+") as f:
    json.dump(address,f,indent=5)
    f.seek(0)
    print(f.read())

file=Path("test12.json")
if file.exists():
    print("File found")
else:
    print("file not found")

ctr=add(4,2)
print(f"Sum of two number is {ctr}")
calculate("Manjeet Singh")