#program with function to find greatest number among 3 
def max(a,b,c):
	if(a>b and a>c):
		return a
	elif(b>c and b>a):
		return b
	else:
		return c;

a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
c=int(input("Enter 3rd number="))

print(max(a,b,c)," is greater")