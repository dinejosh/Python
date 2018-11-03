nums=[10,40,5,2,30,70,90,'abc',300,'python','d']
ind=[3,5,7,9]

imp=[]
for i in ind:
	imp.append(nums[i])
exp= []
for i in nums:
	if i not in imp:
		exp.append(i)

print(imp)
print(exp)

