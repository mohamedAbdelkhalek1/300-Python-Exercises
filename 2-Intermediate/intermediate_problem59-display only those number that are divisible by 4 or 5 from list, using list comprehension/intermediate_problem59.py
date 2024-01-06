"""
intermediate_problem59:

Write a Python Program to display only those number that are divisible by 4 or 5 from list, using list comprehension.   

"""


lst = [2,4,5,6,10,20,40]

new_list = [i for i in lst if i%4 == 0 and i%5 == 0]
print(new_list)