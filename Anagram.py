Text=(input("Enter text for anagram"))
print(Text)
items=Text.split(" ")

print(items)

for i in range(0,len(items)-1):
	items[i]=items[i]+" "+items[i+1]
items.remove(items[-1])
print(items)