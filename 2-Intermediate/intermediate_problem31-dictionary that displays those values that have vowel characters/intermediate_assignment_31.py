"""
intermediate_assignment_31:

Write a Python Program to get 10 number from user to print minimum, maximum and starting, ending number to user.

"""

lst = []

for i in range(4):
    lst.append(int(input(f"Enter Number {i+1} : ")))

print(f"The Maximum Number = {max(lst)}")
print(f"The Minimum Number = {min(lst)}")
print(f"The starting Number = {lst[0]}")
print(f"The ending Number = {lst[-1]}")