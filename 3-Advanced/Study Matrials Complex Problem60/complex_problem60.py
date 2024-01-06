"""
complex_problem60:

Write a Python Program to read any specific line from a file.

"""

file = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem60/input.txt","r")
r = file.readlines()
line = int(input("Enter a line number : ")) 
print(r[line-1]) 