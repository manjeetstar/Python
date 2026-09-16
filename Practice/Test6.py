from pathlib import Path
import json

try:
    with open("../test.txt", "w") as file:
        file.writelines("Add it at the end of the file \n This is the last one \n")        
except FileNotFoundError as e:
    print(e)
else:
    print("This is the else block")
finally:
    print("Rest of the code")

user = {
    "name": "Awatar",
    "age": 421,
    "role": "Dev"
}

with open("../test1.json", "a") as file:
    json.dump(user, file)

for file in Path(".").rglob("*.py"):
    print(file)
