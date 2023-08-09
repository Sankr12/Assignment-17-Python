# Write a python script to get the data type of the set

print()

set1 = set()

num = int(input("Enter the number of elements you want to enter in set: "))

for i in range(num):
    element = input("Enter the element {}: ".format(i+1))
    set1.add(element)

print("Set you made:", set1)

for a in set1:
    try:
        value = eval(a)
        data_type = type(value)
        print("{}: {}".format(a, data_type))
    except (SyntaxError, NameError):
        print("{}: {}".format(a, type(a)))



'''
print()

set1 = set()

num = int(input("Enter the number of elements you want to enter in set: "))

for i in range(num):
    element = input("Enter the element {}: ".format(i+1))
    set1.add(element)

print("Set you made:", set1)

for a in set1:
    print("{}: {}".format(a, type(eval(a))))
'''