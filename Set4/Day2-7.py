from functools import reduce

class CustomRange:
    def __init__(self, start, end):
        self.start=start
        self.end=end 

    def __iter__(self):
        return self
   
    def __next__(self):
        if self.start > self.end:
            raise StopIteration            
        value=self.start
        self.start +=1
        return value

try:
    for i in CustomRange(1,5):
        print(i)
except StopIteration as e:
    print(e)


status=reduce(lambda x,y: x+y, list(map(lambda x: x*x, list(filter(lambda x: x%2 == 0, [1,2,3,5,6,7,8])))))
print(status)