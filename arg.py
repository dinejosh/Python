import sys
print(sys.argv)
print("your filename is"+sys.argv[0]);

print("your inputs are:")
for i in range(1,len(sys.argv)):
	print(sys.argv[i],end=" ")