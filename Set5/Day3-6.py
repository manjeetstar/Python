import os, sys, shutil
from pathlib import Path

print(os.environ.setdefault("name", "Manjeet"))
print(os.environ.get("name"))
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
print(os.listdir("."))

str= os.listdir(".")
for k in str:
    if os.path.isdir(k):
        print(k, sep="-", end=" ")
print("")
print(sys.stdout.write("This is Manjeet "))

Path(".").mkdir(777,exist_ok=True)

