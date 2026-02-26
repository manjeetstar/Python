employee= {"name":"Manjeet", "age":20, "address": "canadaa", "name": "Parul", 4:"false"}
print(employee.get("name1"))
employee.update({"name":"Sanjeet", 4:"whoelse do inknow"})
print(employee)

for k, v in employee.items():
    print(f"key and value pair is  : {k} {v}")

student_name="abcdjfjfjabcdkskkfk"
work_freq={}
for ch in student_name:
    work_freq[ch]=work_freq.get(ch,0)+1
print(work_freq)