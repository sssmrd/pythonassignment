#class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
	length=0
	width=0	
	def area(self):
		return self.length*self.width;
	def __init__(self,l,b):
		self.length=l;
		self.width=b;

x,y=input("Enter length & breadth=").split();
x=int(x);
y=int(y);
ob=Rectangle(x,y);
print("Area of rectangle is ",ob.area());		