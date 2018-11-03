def namehi(myname):#this parameter can be anything anytype list,tuples,class etc
	print("hello "+myname)

namehi("dinesh")	

def avgnum(a):
	sum=0
	for x in a:
		sum=sum+x
	return sum//len(a) #for absolute value
print(avgnum({12,13,25,19}))

#Variable parameters for multiple parameter we use tuple *args

def multiArgs(*args):
	print(args[2])
	print(type(args))
multiArgs("Dinesh","Joshi"," ")	

print(sum((1,2,4,5)))


