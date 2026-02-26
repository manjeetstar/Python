from functools import reduce
import sys
from MyPackage.calculate import add, substract
from MyPackage.display import display

ctr=[2,3,6,5]

result=reduce(lambda x,y: x+y, list(map(lambda x: x*x,list(filter(lambda x: x%2 ==0, ctr)))))
print("Final output is ", result) #

class customException(Exception):
    def __init__(self, message, errorcode):
       super().__init__(message, errorcode)
       self.errorcode=errorcode

def EH():
    try:
        raise customException("Custom exception", 1102)
    except ZeroDivisionError as e:
        print("Error message is ", e)
    except customException as e:
        print("Error descriptio is ", e)   
    finally:
        print("This will be executed always")
        
EH()

add(2,3)
print(substract(10,25))
display()


