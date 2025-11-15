import json
import os
from pathlib import Path

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