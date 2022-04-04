import random

with open("L1.txt","w") as f:
    for i in range(1000000):
        n= random.randint(10000000,99000000)
        f.write(str(n)+ '\n')