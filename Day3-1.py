address="Burnpur cricket club, club Burnpur rambandh, PO-burnpur, dist-burdwan, west bengal, burnpur, club, west"

add=address.split(" ")
addset={}

for a in add:
    addset[a]= addset.get(a,0)+1

print(addset)

print(" ".join(word[::-1] for word in add).title())