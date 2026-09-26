
class CManager:
    def __enter__(self):
        print("Acquiring the resources")
        return "Manjeet Singh"

    def __exit__(self, exc_type, exc, tb):
        print("Cleaning up the resources")
        return True

with CManager() as m:
    print("Main Context Manager code")
    print(f"Returned context is {m}")
    raise ValueError("This is exception")

print("Rest of the code...")