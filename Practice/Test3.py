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
 
ctr=[1,2,3,4,5,6]
ctr1=[ a if a %2 ==0 else 1 for a in ctr ]
print(ctr1)

ctr2 =[ b*b for b in [ a for a in ctr if a%2 ==0 ]]
print(ctr2)

ctr3={b: "element" if type(employee[b]) != dict else "dict" for b, value in employee.items()}
print(ctr3)
print(type(employee["dept"]))
