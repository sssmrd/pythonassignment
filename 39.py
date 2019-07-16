#program to remove item(s) from set
l=input("Enter some elements=").split();
s=set(l);
print(s)
r=input("Enter elements to be removed=").split();
for i in r:
	s.discard(i)
print(s)