import sys
import time
import os
import math


def union(f_1, f_2):
    l1 = {}
    l2={}
    l3={}
    """
    Finding the union of two dictionaries

    Args:
    file_1 file_2 (dict):dictionaries to find union

    Returns:
    dictionaries of union of two dictionaries

    """
    for i in f_1:
        if (i == None):
            l1[i] = 1

    for j in f_2:
        l2[j] = 1
    lp=abs(len(l2)-len(l1))
    return (lp)




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
    if (os.path.exists(y)):
        return (y)


def checkEmail(s):
    s = s.strip()
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
                hm[email] = "true"

    return hm


def write_file(result):
    a = time.time()
    print(str(sys.argv[1]) + " " + str(len(l1)) + " emails," + str(sys.argv[2]) + " " + str(
        len(l2)) + " emails," + " " + str(sys.argv[3]) + " " + str(
        result) + " emails; " + "Time taken: " + str(a - f) + " seconds")
    # print(result)


f = time.time()
if __name__ == "__main__":
    l1_file = validate_args(sys.argv[1])
    l2_file = validate_args(sys.argv[2])
    ret_file = validate_args(sys.argv[3])

    # l2_file=validate_args(sys.argv[1])
    # ret_file=validate_args(sys.argv[2])

    l1 = read_file(l1_file)
    l2 = read_file(l2_file)

    result = union(l1, l2)
    write_file(result)


# import sys
# import time
# import os.path
#
# l1={}
# l2={}
# def union(f_1,f_2):
#
#
#     s = len(f_1)
#     d = len(f_2)
#     for i in range(0, s):
#         if (l1.get(f_1[i]) == None):
#             l1.update({s: i})
#     for i in range(0, d):
#         if (l1.get(f_2[i]) == None and l2.get()):
#             l2.update({s: i})
#     return (len(l2)-len(l1))
#
#
#
#
#
# def split(word):
#     l1.update()
#     return list(word)
# def checkEmail(s):
#     # k=split(s)
#     # #d=k[1]
#     # #print(ord(d))
#     # count=0
#     # k1=0
#     # g=0
#     # gn=0
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
#
#
#
#                     continue
#         if(ord(i)==46):
#             count=count+1
#             if((k1==1) and(g==2)):
#                 continue
#     if(k1==1)and(g==2):
#         return True
#     else:
#         return False
#
#
#
#
#
# # emails=[]
# # emails1=[]
# # hm={}
# # l2={}
# # hm3={}
# # hm33={}
# # r1=0
# # r2=0
#
# f = time.time()
# def validate_args(argv):
#
#     if(os.path.exists(argv)):
#         return (argv)
#
#     # if(len(argv)!=None)
#     #     return l1_file
#
#
# def read_file(l1_file):
#
#     fh = open(l1_file, "r")
#     try:
#         return l1_file.read()
#     finally:
#         l1_file.close()
#
#
#
#
#     # emails=[]
#     # with open("l1_file.txt",'r') as f12:
#     #     for email in f12.readlines():
#     #         emails.append(email)
#     #     r1=len(emails)
#     #
#     #
#     #
#     #
#     # if(r1>0):
#     #     return(l1_file)
#
#
#
#     for i in range(0,l1_file):
#
#         d11=checkEmail(emails[i])
#         if(d11==True):
#
#             union(emails[i],i)
#
#
#
#
# def read_file(l2_file):
#
#
#     emails1=[]
#
#     with open("l2_file.txt", 'r') as f2:
#         for email in f2.readlines():
#             emails1.append(email)
#         r2 = len(l2_file)
#     for i in range(0, r2):
#         hm3 = {emails1[i], i}
#         d111 = checkEmail(emails1[i])
#
#         if (d111 == True):
#
#             union(emails1[i], i)
#
#
# a=time.time()
# def write_file(result):
#     #print(str(sys.argv[1])+" "+str(r1)+" emails,"+str(sys.argv[2])+" "+str(r2)+" emails,"+" "+str(sys.argv[3])+" "+str(len(l1))+" emails; "+"Time taken: "+str(a-f)+" seconds")
#     print(result)
# def main():
#     if __name__=="__main__":
#         l1_file,l2_file,ret_file=validate_args(sys.argv)
#         l1=read_file(l1_file)
#         l2=read_file(l2_file)
#         result=union(l1,l2)
#         write_file(result)