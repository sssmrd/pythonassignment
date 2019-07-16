#program to add an item in a tuple.
l=input("Enter the values in tuple=").split();
print("Before adding")
t=tuple(l)
print(t)
val=input("Enter item to be entered=")
l=list(t)
l.append(val);
t=tuple(l)
print("After adding")
print(t)