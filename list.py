emp=[]

length = int(input("enter the length of list"))
for i in range(0,length):
	choice=(input("Enter your choice 1.To enter String value 2.To enter integer value"))
	if(choice=='1'):
		element=input("enter String element")
	if(choice=='2'):
			element=int(input("Enter  number"))
	emp.append(element)
print(emp)	