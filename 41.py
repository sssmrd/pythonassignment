#create an array of 5 integers and display the array items. Access individual element through indexes.
import array;
num=array.array("i",[0,0,0,0,0])
l=input("Enter 5 numbers=").split();
nl=list();
for i in range(0,len(l)):
	nl.append(int(l[i]));
ar=array.array("i",nl)
for i in range(0,len(nl)):
	print(ar[i])