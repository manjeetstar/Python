import re
m=re.findall(r"\d+", "This is India 911 code and its 323 districts")
print(m)

m1=re.split(r":\s","Manjeet and Parul : Awatar Aditi")
print(m1[0])


for m2 in re.finditer(r"(\d+)-(\d+)\s", "929-77272 83-9292 92-9292 "):
    print(m2.groups())

str="This is Manjeet and Manjeet needs to work hard"
m3=re.sub(r"\s(Manj\w+)\s", " Parul ",str, 1)
print(m3)

m4=re.search(r"(?P<name>\sManj\w+\s)", str)
print(m4.group("name"))

m5="manjeetikon-101@gmail.com"
m = re.match(r"^([\w.-]+)@([\w.-]+)\.(\w{2,})$", "manjeetikon-101@gmail.com")
print(m.group(3))
