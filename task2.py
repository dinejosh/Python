strp=int(input("enter start number"))
endp=int(input("enter end number"))
l1=[]

l2=[]
for i  in range(strp,endp+1):
    l1.append(i)
    l2.append(i*i)

dictnew=dict(zip(l1,l2))

print(dictnew)
