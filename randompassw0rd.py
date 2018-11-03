import random
passw0rd=''
name=input('enter a name')
user={}
#def genchar(n):
#	chars=[]
#	for i in range(n//2):
#		chars=chars.append(str(chr(random.randint(65,91))))
#		chars=chars.append(str(chr(random.randint(97,122))))
#	random.shuffle(chars)
#	chars="".join(chars)
#	print(chars)
def usercheck(name):
	if name not in user.keys():
		return True
	else:
		print("User aready exist")

def genc(n):
	chars=[]
	for i in range(65,90):
		chars.append(str(chr(i)))
	for i in range(97,122):
		chars.append(str(chr(i)))	

	random.shuffle(chars)
	chars="".join(random.sample(chars,k=n))	
	return chars
def gennum(n):
	nums=""
	for i in range(n):
		nums=nums+str(random.randint(0,9))
	return nums

def finalPass(name):
	if usercheck(name):
		passw0rd=gennum(4)+genc(4)+gennum(4)+genc(4)
		user[name]=passw0rd

finalPass(name)
print(user)

