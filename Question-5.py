# Write a python script to add items from another set to the current set. thisset = {"Java", "Python", "SQL"} 
# secondset = {"C", "Cpp", "NoSQL"}

print()
thisset = {"Java", "Python", "SQL"}
secondset = {"C", "Cpp", "NoSQL"}

for i in secondset:
    thisset.add(i)

print(thisset)
print()