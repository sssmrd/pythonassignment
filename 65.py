#program to get the class name of an instance in Python
class Rectangle:
	length=0
	width=0	
	def area(self):
		return self.length*self.width;
	def __init__(self,l,b):
		self.length=l;
		self.width=b;
class Square:
	side=0	
	def area(self):
		return self.side*self.side;
	def __init__(self,s):
		self.side=s;
class  Circle:
	radius=0;
	def area(self):
		return self.radius*3.142*self.radius;
	def __init__(self,r):
		self.radius=r;
o1=Rectangle(10,20);
o2=Square(5);
o3=Circle(4);
print(type(o1))
print(type(o2))
print(type(o3))