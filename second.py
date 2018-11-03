n=(input("enter your number"))
count=0
if n.isnumeric():
	n=int(n)
	for i in range(1,int(n)+1):
		if n%i==0:
			print(i,end=" ")
			count=count+1
		if count>2:
			print("")	