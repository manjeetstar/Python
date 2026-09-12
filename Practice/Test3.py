employee={
    "name": "Manjeet",
    "age":20,
    "isMarried": False,
    "dept":{
        "deptName":"HRMS",
        "Location": "Canada"
    }
}
print(employee["dept"].get("Location"))

for key, value in employee.items():
    print(f"key: {key} and its value is {value}")

employee["dept"]["Location"]="United states"
print(employee["dept"].get("Location"))