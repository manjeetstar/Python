name="Manjeet"
age=12
isMarried=False

print(name, age, isMarried, sep=" : ", end =" ")
print("Manjeet Singh")
print(f"Name of candidate is {name} of age {age} and marital status is {isMarried}")

if age>20:
    print("age is greater than 20")
elif age<10:
    print("age is less than 10")
elif age>5 and age<20:
    print("Age is greater than 5 but lesser than 20")
else:
    print("God know that whats the age of candidate")