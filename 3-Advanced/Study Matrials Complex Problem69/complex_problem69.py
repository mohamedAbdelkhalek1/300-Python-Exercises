"""
complex_problem69:

Write a Python Program To get 10 number from user to store in a list and find sum, product, min, max, last and first from number.
Display each result in a file.

"""
from math import prod

file = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem69/listfile.txt","w")

lst = []
for i in range(10):
    lst.append(int(input("Enter a number")))


sum = sum(lst)

product = prod(lst)

max = max(lst)
min = min(lst)

last_e = lst[-1]
first_e = lst[0]

file.write("List items are = "+str(lst)+" \n")
file.write("List Max = "+str(max)+" \n")
file.write("List Min = "+str(min)+" \n")
file.write("List sum = "+str(sum)+" \n")
file.write("List Product = "+str(product)+" \n")
file.close()