import sys
import time
import os


l1={}
def union(f_1,f_2):

    s=len(f_1)
    d=len(f_2)
    for i in range(0,s):
        if (l1.get(f_1[i])==None):
            l1.update({s:i})
    for i in  range(0,d):
        if (l1.get(f_2[i])==None):
            l1.update({s:i})
    return (l1)



def split(word):
    l1.update()
    return list(word)
def checkEmail(s):
    k=split(s)
    d=k[1]
    print(ord(d))
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


f = time.time()
def validate_args(sys.argv):
    if(os.path.exists(y)):
        return (y)
    

def read_file(l1122_file):
    emails1=[]
    fl={}

    with open(l1122_file, 'r') as f2:
        for email in f2.readlines():
            emails1.append(email)
        r2 = len(l1122_file)
        for i in range(0, r2):
            hm3 = {emails1[i], i}
            d111 = checkEmail(emails1[i])

            if (d111 == True):

                fl.update(l2_file)
            return (fl)


a=time.time()
def write_file(result):
    #print(str(sys.argv[1])+" "+str(r1)+" emails,"+str(sys.argv[2])+" "+str(r2)+" emails,"+" "+str(sys.argv[3])+" "+str(len(l1))+" emails; "+"Time taken: "+str(a-f)+" seconds")
    print(result)
if __name__=="__main__":
    l1_file,l2_file,ret_file=validate_args(sys.argv)

    # l2_file=validate_args(sys.argv[1])
    # ret_file=validate_args(sys.argv[2])

    l1=read_file(l1_file)
    l2=read_file(l2_file)
    result=union(l1,l2)
    write_file(result)