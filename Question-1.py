# Write a python script to store all the programming languages known to you using set
'''
print()
Language = input("Enter your known language separated by comma: ")
s1 = {e for e in Language.split(',')}
print(s1)
print()'''

print()
num = int(input("Enter the number of language you want to write: "))
i=0
s1 = set()
while i<num:
    e = input("Enter the {} language: ".format(i+1))
    s1.add(e)
    i+=1
print(s1)
print()