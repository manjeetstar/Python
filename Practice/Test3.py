ctr= [10,20,30,40,"Manjeet Singh", [11,12,3,45,5,6]]

ctr1=[ctr[a] for a in range(len(ctr[0:3]))]
print(ctr1)
ctr.append("awatar")
print(ctr)
ctr.extend(["awatar",20,False])
print(ctr)