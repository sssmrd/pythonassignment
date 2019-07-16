#program to remove duplicates from a list.
l=['abc', 'xyz', 'aba', '1221','xyz','abc']
print("Before")
print(l)
l=list(dict.fromkeys(l))
print("After");
print(l)
