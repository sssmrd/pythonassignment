#program to remove an item from a set if it is present in the set
l=input("Enter some elements=").split();
s=set(l);
print(s)
r=input("Enter elements to be removed=").split();
for i in r:
	try:
		s.remove(i)
	except KeyError:
		print(i," not present")
print(s)