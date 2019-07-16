#program to append a new item to the end of the array.
import array;
num=array.array("i",[0,0,0,0,0])
l=input("Enter 5 numbers=").split();
nl=list();
for i in range(0,len(l)):
	nl.append(int(l[i]));
ar=array.array("i",nl)
for i in range(0,len(ar)):
	print(ar[i])
val=int(input("Enter the value to append="))
ar.append(val);
for i in range(0,len(ar)):
	print(ar[i])