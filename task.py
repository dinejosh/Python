import sys
emp=[]
leng=int(len(sys.argv))
for i in range(1,leng-1):
		emp.append(sys.argv[i])
print(emp)		


N=(10,20,30,40,50)
comList=[0]
for i in N:
	comList.append(i+comList[-1])
comList.remove(0)	
	
print(comList)