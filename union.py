import sys
import time
import os



def union(f_1,f_2):
    """
    Finding the union of two dictionaries

    Args:
    file_1 file_2 (dict):dictionaries to find union

    Returns:
    dictionaries of union of two dictionaries

    """
    l1 = {}
    for i in f_1:
        l1[i] = 1
    for j in f_2:
        l1[j] = 1
    return (l1)



# def split(word):
#     l1.update()
#     return list(word)
# def checkEmail(s):
#     k=split(s)
#     d=k[1]
#     print(ord(d))
#     count=0
#     k1=0
#     g=0
#     gn=0
#     for i in k:
#         if(gn==1):
#             if(ord(i) in range(48,57)):
#                 return False
#         if((g==0) and (k1==0)):
#             if(ord(i) in range(48,57)):
#                 return False
#         if(g==3):
#             if(ord(i) in range (48,57)):
#                 return False
#         if(ord(i) in range(97,122)or(ord(i) in range(65,90))):
#             if(g==0) and (k1==0):
#
#                 k1=1
#             continue
#         if(ord(i)==45):
#             if(ord[i+1] in range(97,122)):
#                 continue
#         if(ord(i)==64):
#             g=3
#             gn=1
#             if(k1==1):
#                 g = 2
#                 if(k1==1):
#                     continue
#         if(ord(i)==46):
#             count=count+1
#             if((k1==1) and(g==2)):
#                 continue
#     if(k1==1)and(g==2):
#         return True
#     else:
#         return False


f = time.time()
def validate_args(y):
    if(os.path.exists(y)):
        return (y)
    
def checkEmail(s):



    s=s.strip()
    k = list(s)
    count = 0
    k1 = 0
    g = 0
    gn = 0
    for i in k:
        if (gn == 1):
            if (ord(i) in range(48, 57)):
                return False
        if ((g == 0) and (k1 == 0)):
            if (ord(i) in range(48, 57)):
                return False
        if (g == 3):
            if (ord(i) in range(48, 57)):
                return False
        if (ord(i) in range(97, 122) or (ord(i) in range(65, 90))):
            if (g == 0) and (k1 == 0):
                k1 = 1
            continue
        if (ord(i) == 45):
            continue
        if (ord(i) == 64):
            g = 3
            gn = 1
            if (k1 == 1):
                g = 2
                if (k1 == 1):
                    continue
        if (ord(i) == 46):
            count = count + 1
            if ((k1 == 1) and (g == 2)):
                continue
    if (k1 == 1) and (g == 2):
        return True
    else:
        return False


def read_file(l1_file):

    """
    Read the file line by line, check validity of the email, and returns a list of valid emails

     Args:
        li_file(str): Name of the file to read

     Returns:
        (dict): a collection of valid emails

     """
    hm = {}
    with open(l1_file, 'r') as f2:
        for email in f2.readlines():
            if checkEmail(email):
                hm[email]="true"

    return hm


def write_file(result):

    a=time.time()

    print(str(sys.argv[1]) + " " + str(len(l1)) + " emails," + str(sys.argv[2]) + " " + str(
        len(l2)) + " emails," + " " + str(sys.argv[3]) + " " + str(
        len(result)) + " emails; " + "Time taken: " + str(a - f) + " seconds")




    # print(str(sys.argv[1])+" "+str(len(l1_file))+" emails,"+str(sys.argv[2])+" "+str(len(l2_file))+" emails,"+" "+str(sys.argv[3])+" "+str(len(result))+" emails; "+"Time taken: "+str(a-f)+" seconds")
    # #print(result)
f=time.time()
if __name__=="__main__":
    l1_file=validate_args(sys.argv[1])
    l2_file=validate_args(sys.argv[2])
    ret_file=validate_args(sys.argv[3])

    # l2_file=validate_args(sys.argv[1])
    # ret_file=validate_args(sys.argv[2])

    l1=read_file(l1_file)
    l2=read_file(l2_file)

    result=union(l1,l2)
    write_file(result)