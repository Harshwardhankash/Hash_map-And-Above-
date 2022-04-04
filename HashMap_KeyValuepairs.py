hm={};
hm["Abhi"]=True
hm["jeet"]=False
hm={'Abhi':True,"jeet":False}
print(hm)
i=len(hm)
s="Pradeep" in hm
print(s)
s=hm["Abhi"]
print(s)

for key,value in hm.items():
    print(key,value)