sets={"Dinesh","Joshi",3,4,4,5}

l1=[i+i for i in sets]
print(type(sets))
print(l1)
dictr=dict(zip(sets,l1))
print(dictr)


sets.add("complex") #sets add element method
sets.remove("Dinesh")
sets.discard("Dinesh")
print(sets)

sets.clear()
print(type(sets))

s1={1,2,4,5,6,7,8,0}
s2={5,6,8,9,10,22}
s3={5,6,7}

print(s1.union(s2))     # |- is union
print(s1.intersection(s2)) # & - is intersection
print(s3.issubset(s1)) # >
print(s1.issuperset(s2)) # <        
print(s2.difference(s1)) # -
print(s1.isdisjoint(s3))# ^

print(s1^s2)

