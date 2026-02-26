from collections import namedtuple, deque, defaultdict, Counter

Point=namedtuple("Point",["name", "age"])
p=Point("Manjeet", 20)

print(p.name, p.age)

for a in p:
    print(a)

d1=deque([1,2,4,5])
d1.rotate(2)
print(d1)

d1=defaultdict(list)
d1["a"].append("apple")
d1["a"].append("guava")
d1["c"].append("apple")

print(d1)

d1=Counter("Manjeet Singh")
print(d1.most_common(10))
