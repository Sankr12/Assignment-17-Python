# Write a python program to remove last item of the given set 
# thisset = {"Python", "Django", "JavaScript", "SQL"}

print()

thisset = {"Python", "Django", "JavaScript", "SQL"}
print("Original set: {}".format(thisset))

li = list(thisset)
li.pop()
thisset = set(li)
print("After removing last item of given set: {}".format(thisset))

print()