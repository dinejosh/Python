dictn={1:'Dinesh',2:'Joshi'}
print(dictn)

dictn['tech']='java'
print(dictn)

x=dictn.popitem()
print(dictn,x)
dictn.fromkeys
print(dictn.fromkeys)

for i in dictn.values(): #ithervalues in 2.7
    print(i)
for i in dictn.keys():#iterkeys
    print(i)
l1=(1,2,3,4)
l2=("one","two","Three","four")

dic1={}
if len(l1)==len(l2):
    for i in range(0,len(l1)):
        dic1[l1[i]]=l2[i]
    print(dic1)

a=zip(l1,l2)
a=dict(a)
print(a)



