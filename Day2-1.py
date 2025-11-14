names=["Manjeet", "Sanjeet","Kamal","Manjeet"]
names[1:3]=["Parul","Charu"]
print(names)

names.insert(0,"Manjeetstar")
print(names.count("Manjeet"))
names.extend(["Awatar", "Rani"])
print(names)


names= [name.upper() for name in names if name == "Manjeet"]
print(names)

address="Cricket club, rambandh, burnpur"

add_vowel=sum([vow in "aeiou" for vow in address])
print(f"Available vowels are {add_vowel}")

ages=(1,2,3,4,5,6,7)

a,b,c,d,e,f,g=ages
print(f"Name of the candidate is {a}")
print(ages[2:-1])

