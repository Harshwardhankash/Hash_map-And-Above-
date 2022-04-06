import sys
import time
import random
import string
# import random
#
# with open("L2334.txt","w") as f:
#     for i in range(1000000):
#         n= random.randint(10000000,99000000)
#         f.write(str(n)+ '\n')
#
# n= random.randint(10000000,99000000)
# print(n)
# x = random.randint(3,7)
# print(x)
#
hm1={}
hm2={}
r1=0
r2=0
def unon(s,i):
    if (hm1.get(s)==None and i<r1):
        hm1.update({s:i})
    if (i >= r1):
        if (hm1.get(s) == None and i >= r1 and i < r2 and hm2.get(s) == None):
            hm2.update({s: i})




def split(word):
    hm.update()
    return list(word)
def checkEmail(s):
    k=split(s)
    #d=k[1]
    #print(ord(d))
    count=0
    k1=0
    g=0

    for i in k:

        if(ord(i) in range(97,122)or(ord(i) in range(65,90))):
            if(g==0) and (k1==0):

                k1=1
            continue
        if(ord(i)==45):
            if(ord[i+1] in range(97,122)):
                continue
        if(ord(i)==64):

            if(k1==1):
                g = 2
                if(k1==1):



                    continue
        if(ord(i)==46):
            count=count+1
            if((k1==1) and(g==2)):
                continue
    if(k1==1)and(g==2):
        return True
    else:
        return False





emails=[]
emails1=[]
hm={}
hm2={}
hm3={}
hm33={}
r1=0
r2=0

def random_char(N):
    N=random.randint(0,7)
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))


    return res


with open("L1.txt","w") as f11:
    for i in range(random.randint(0,1000000)):
        d=random_char(random.randint(7, 8)) + "@" + random_char(random.randint(7, 8)) + ".com"
        f11.write(str(d)+'\n')


with open("L2.txt","w") as f111:
    for i in range(random.randint(0,1000000)):
        d1=random_char(random.randint(7,8)) + "@" + random_char(random.randint(7,8)) + ".com"
        f111.write(str(d1) + '\n')
        # f111.write(random_char(7)+"@"+str(random_char(7))+".com")




with open("L1.txt",'r') as f12:
    for email in f12.readlines():
        emails.append(email)
    r1=len(emails)

for i in range(0,r1):

    d11=checkEmail(emails[i])
    if(d11==True):

        unon(emails[i],i)

with open("L2.txt", 'r') as f2:
    for email in f2.readlines():
        emails1.append(email)

    r2 = len(emails1)


for i in range(0, r2):

    hm3 = {emails1[i], i}
    d111 = checkEmail(emails1[i])

    if (d111 == True):

        unon(emails1[i], i)


a=time.time()
print(str(sys.argv[1])+" "+str(r1)+" emails,"+str(sys.argv[2])+" "+str(r2)+" emails,"+" "+str(sys.argv[3])+" "+str(len(hm2))+" emails; "+"Time taken: "+str(a)+" seconds")
