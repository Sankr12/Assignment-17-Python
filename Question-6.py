# Write a python program to add elements of a list to a set 
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

print()
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

for i in mylist:
    thisset.add(i)

print(thisset)
print()