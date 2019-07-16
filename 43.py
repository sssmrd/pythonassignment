#program to reverse the order of the items in the array.
import array;
num=array.array("i",[0,0,0,0,0])
l=input("Enter 5 numbers=").split();
nl=list();
for i in range(0,len(l)):
	nl.append(int(l[i]));
ar=array.array("i",nl)
for i in range(0,len(ar)):
	print(ar[i])
ar.reverse()
print("Reversed array")
for i in range(0,len(ar)):
	print(ar[i])