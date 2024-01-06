"""
complex_assignment_65:

Write a Python Program to create a list from existed list which display items without start and end char.

"""
my_list = ["Ahmed", "Asmaa", "Mohammed"]

new_list = [item[1:len(item)-1] for item in my_list]

print(new_list)