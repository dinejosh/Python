endp=int(input("enter endpoint"))
l1=[]
l2=[]
l3=[]
l4=[]
for i in range (1,endp+1):
    l1.append(i)
    l2.append(i*i)
    if i%2 ==0:
        l3.append(i)
        l4.append(i*i)


print(l1,l2,l3,l4)        

#same thing can be done in list comprehension

a1=[i for i in range(1,11)]
a2=[i**2 for i in range(1,11)]

a3=[i for i in range(1,11) if i%2==0]

a4=[i*i for i in range(1,11) if i%2==0]

print (a1,a2,a3,a4)

#Dictionary comprehenssion

words=["java","Python","C++"]
l={i:len(i) for i in words if type(i)!=int}

print(l)
