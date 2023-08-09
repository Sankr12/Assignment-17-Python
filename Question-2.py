# Write a python script to print your own information {name, age, gender, so on...}

print()
s1 = {'Name', 'Age', 'Gender', 'Class', 'Colour', 'Odour', 'Caste'}
s2 = set()

for i in s1:
    a = input("Enter your {}: ".format(i))
    s2.add(a)
print("Your info:",s2)
print()