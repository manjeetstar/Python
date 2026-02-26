def Method1(cls):
    print("Decorating class: ", cls.__name__)
    original_display=cls.display

    def new_display(*args, **kwargs):
        print("Implemenation of new Display method")
        ctr=[x**2 if isinstance(x, (int, float)) else x for x in args]
        result=original_display(*ctr)
        print("Sum of two number is ", result)
        return result
    cls.display=new_display
    return cls

@Method1
class display:
    def display(self,a,b):
        return a+b
    
d1=display()
d1.display(5,10)
print(display.__dict__)