alist=[1,2,'a','python',400,[1,20,'a'],40]
allitems=[]
for i in alist:
	if type(i)==list:
		for j in i:
			allitems.append(j)
	else:
		allitems.append(i)
print(allitems)