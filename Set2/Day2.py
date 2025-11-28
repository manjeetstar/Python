name="Manjeet Singh Phull aeiou"
print(name[3:-8:-1])

vowel, count ="aeiou", 0


for c in name:
    if c in vowel:
        count +=1

print(f"No of vowels is {count}")