
"""
intermediate_assignment_64:

Write a Python program to insert an element after each element of a list.

"""

lst = [1,2,3,34,4,5,6,7,8,9,10]
print(lst)
num = int(input("Enter a element"))
new_list = [ str(i)+" "+str(num) for i in lst]
print(new_list)
for i in new_list:
    print(i)