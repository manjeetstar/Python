try:
    with open("../test1.txt","a") as f:
        pos=f.tell()
        print("Current Position: " , pos)       
        f.write("This is first line checking writing and seek and tell part \n")
except FileNotFoundError as e:
    print("Error message ", e)
finally:
    print("This will be executed always")
