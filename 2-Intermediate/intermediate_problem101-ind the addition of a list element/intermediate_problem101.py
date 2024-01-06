"""
intermediate_problem101:

Write a Python Program to find the addition of a list element to create a new list.
Add element of list as 1st and 2nd, 2nd and 3rd, 3rd and 4th …

"""


lst = []

n = int(input("Enter a length of the list "))

for i in range(n):
    item = int(input(f"Enter a number {i+1} : "))
    lst.append(item)
print(lst)

new_list = []

for i in range(n-1): # 6
    item = lst[i] + lst[i+1]
    new_list.append(item)
print(new_list)