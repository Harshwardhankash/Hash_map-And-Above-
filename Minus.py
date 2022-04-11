import sys
import time

hm1={}
hm2={}
r1=0
r2=0
count=0
def unon(s,i):
    if (hm1.get(s)==None and i<r1):
        hm1.update({s:i})
    if (i >= r1):
        if (hm1.get(s) == None and i >= r1 and i < r2 and hm2.get(s) == None):
            hm2.update({s:i})




def split(word):
    hm.update()
    return list(word)
def checkEmail(s):
    k=split(s)
    count=0
    k1=0
    g=0
    gn = 0
    for i in k:
        if(gn==1):
            if(ord(i) in range(48,57)):
                return False
        if((g==0) and (k1==0)):
            if(ord(i) in range(48,57)):
                return False
        if(g==3):
            if(ord(i) in range (48,57)):
                return False
        if(ord(i) in range(97,122)or(ord(i) in range(65,90))):
            if(g==0) and (k1==0):

                k1=1
            continue
        if(ord(i)==45):
            if(ord[i+1] in range(97,122)):
                continue
        if(ord(i)==64):
            g=3
            gn=1
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



f=time.time()

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
print(str(sys.argv[1])+" "+str(r1)+" emails,"+str(sys.argv[2])+" "+str(r2)+" emails,"+" "+str(sys.argv[3])+" "+str(len(hm1)-len(hm2))+" emails; "+"Time taken: "+str(a-f)+" seconds")
