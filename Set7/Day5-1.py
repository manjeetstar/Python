from contextlib import contextmanager

class CM:
    def __enter__(self):
        print("Entering into the operation")
        # raise FileNotFoundError("File not found")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("Exception Occured ", exc_type, traceback)
        else:
            print("All went smooth")

with CM() as f:
    print("Operation need to be finished")

@contextmanager
def open_db(path):
   f=open(path)
   try:
       yield f
   except Exception as e :
       print("Exception occoured.", e)
   finally:
       f.close()

with open_db("../test.txt") as f:
    print(f.readline())
    print(f.readline())