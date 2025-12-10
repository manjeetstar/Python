from functools import reduce
class ListAddition:  
    def __add__(self, other):
        print("Addition operator of tuple")
        sum = reduce(lambda x,y: x+y, other)
        return sum

c=ListAddition()
print(c + [1,2,4,65])    

