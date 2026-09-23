import sys, tracemalloc
tracemalloc.start()
ctr=["Manjeet",22,3,4,True]

for stat in tracemalloc.take_snapshot().statistics("lineno")[:5]:
    print(stat)

x=10
print("Initial value ", id(x))

x=20
print("After ", id(x))