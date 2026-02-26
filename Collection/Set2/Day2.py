from collections import namedtuple

names=["Manjeet",20, "Parul", False, "Awatar", "Manjeet"]

details = [name for name in names if type(name) == str]
print(details)

a=names.count("Manjeet")
print(a)

x=[x for x in range(1,100) if x%2 ==0]
print(x)

ctr=[y for y in "abchjdlfooqroqroqowhr" if y in "aeiou"]
print(f"No. of vowels present in string is {len(ctr)}")

names.extend(["A",8,3,3,2])
print(names)

nTuple=("Manjeet",10,20,"Awatar", False,"Satyam")
print(nTuple)

Candidate=namedtuple("Candidate", "name address city zip")
n=Candidate("Manjeet", "Canada","Vancouver", 20220)

print(n.name, n.address, n.city, n.zip, end=" ")


