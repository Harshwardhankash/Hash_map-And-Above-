try:
     #emails=handler.read(jh.py)
     with open("Kand.txt","r") as f:
         f.read()

     #f = open("ReadingFromaFile.py", "r")
     # print(f.read())
except FileNotFoundError as e:
    print("File {0}: read error: {1}".format("Kand.txt",e))
except Exception as e1:
    print("Generic error: {0}".format(e1))
raise Exception("I am Down,please help me")

# a=5
# b=0
# try:
#     print("resource Open")
#     print(a/b)
#     k=int(input("Enter a number"))
# except Exception as e:
#     print("Hey ,You cannot divide a number by zero",e)
# finally:
#     print("resouce closed")



