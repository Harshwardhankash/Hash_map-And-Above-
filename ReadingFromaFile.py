# import random
#
# with open("L1.txt","w") as f:
#     for i in range(1000000):
#         n= random.randint(10000000,99000000)
#         f.write(str(n)+ '\n')

#n= random.randint(10000000,99000000)
#print(n)
# x = random.randint(3,7)
# print(x)




emails=[]
with open("tax",'r') as f:
    for email in f.readlines():
        emails.append(email)
print(emails)