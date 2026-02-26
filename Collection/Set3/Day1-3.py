employee={"name":"Manjeet", "age":20,
          "address":{
              "address1": "Vancouver",
              "city": "Montreal",
              True: 1
          }}

for k, v in employee.items():
    print(k, v)

print(employee["name"], employee["address"].get("address1"))
print(employee.get("Address2"))

name="shddfshsfhskhfkshfksdhfhskdhf"
d={}

for k in name:
    d[k]=d.setdefault(k,0)+1

print(d, end="", sep="-")

s1={name:name.upper() for name in ["Manjeet", "Parul", "Aditi"] }
print(s1, sep="\n")