"""
intermediate_assignment_71:

Write a Python program to multiply with every number with user entered number in a list.  When Number is Even

"""
lst = [1,2,3,-4,5,-3,9,-8]
print(lst)

n = int(input("Enter an even number"))

if n%2==0:
   new_list = [n*i for i in lst]
   print(new_list)
else:
    print("Not Even Number")