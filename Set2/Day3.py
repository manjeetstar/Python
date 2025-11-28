employee={"name":10, "Address": 123, "age":20}
print(employee)
employee.update({"country":"Canada"})
print(employee)
employee["name"]="Ajay"
print(employee.get("name1"))

name="qrqqqrwqwrqwr"
ctr={}

for k in name:
    ctr[k]= ctr.setdefault(k,0)+1

print(ctr)

for k1, k2 in ctr.items():
    print(k1, " ", k2)

