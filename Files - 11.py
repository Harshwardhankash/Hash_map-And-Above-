import random
import string
def random_char(N):
    N=7
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))


    return res

with open("L1.txt","w") as f11:
    for i in range(random.randint(0,1000000)):
        d=str(random_char(random.randint(0,320))+"@"+str(random_char(random.randint(0,320)))+"."+str(random_char(random.randint(0,320))))
        f11.write(str(d) + '\n')


with open("L2.txt","w") as f111:
    for i in range(random.randint(0,1000000)):
        d1=str(random_char(random.randint(0,320))+"@"+str(random_char(random.randint(0,320)))+"."+str(random_char(random.randint(0,320))))
        f111.write(str(d1) + '\n')
        # f111.write(random_char(7)+"@"+str(random_char(7))+".com")