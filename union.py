import sys
import time

l1={}
def union(s,i):
    if (hm1.get(s)==None):
        hm1.update({s:i})



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
    gn=0
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
l2={}
hm3={}
hm33={}
r1=0
r2=0

def main():

if _name_=="__main__":
    l1_file,l2_file,ret_file=validate_args(argv)
    l1=read_file(l1_file)
    l2=read_file(l2_file)
    result=union(l1,l2)
    write_file(result)


f = time.time()
with open("l1_file.txt",'r') as f12:
    for email in f12.readlines():
        emails.append(email)
    r1=len(emails)

validate_args(argv):

return l1_file


    if(r1>0):
        return(l1_file)
return (l1_file)


for i in range(0,r1):

    d11=checkEmail(emails[i])
    if(d11==True):

        union(emails[i],i)






with open("l2_file.txt", 'r') as f2:
    for email in f2.readlines():
        emails1.append(email)

    r2 = len(emails1)
validate_args(argv):
return (l2_file)

for i in range(0, r2):

    hm3 = {emails1[i], i}
    d111 = checkEmail(emails1[i])

    if (d111 == True):

        union(emails1[i], i)


a=time.time()

print(str(sys.argv[1])+" "+str(r1)+" emails,"+str(sys.argv[2])+" "+str(r2)+" emails,"+" "+str(sys.argv[3])+" "+str(len(l1))+" emails; "+"Time taken: "+str(a-f)+" seconds")
