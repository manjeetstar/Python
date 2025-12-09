from functools import reduce

ctr=[2,3,6,5]

result=reduce(lambda x,y: x+y, list(map(lambda x: x*x,list(filter(lambda x: x%2 ==0, ctr)))))
print("Final output is ", result) #

