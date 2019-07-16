#function to check whether a number is in a given range
def ckrng(x,y,n):
	if n in range(x,y+1):
		print(n," in range",x,y)
	else:
		print(n," not in range",x,y)

x,y=input("Enter start and end of range=").split()
x=int(x)
y=int(y)
n=int(input("Enter a number="))
ckrng(x,y,n)
