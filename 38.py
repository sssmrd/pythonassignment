#program to add member(s) in a set.
l=input("Enter some elements=").split();
s=set(l);
print(s)
c=int(input("How many elements to enter="))
for i in range(0,c):
	n=input("Enter the element to be added in set=")
	s.add(n);
print(s)