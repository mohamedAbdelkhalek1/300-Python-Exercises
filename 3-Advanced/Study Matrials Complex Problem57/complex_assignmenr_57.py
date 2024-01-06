"""
complex_assignmenr_57:

Write a Python Program to Read content from one file and write it into another file. Except a specific string, that is taken from user.

"""

input = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem57/input.txt","r")
output = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem57/output.txt","w")

for line in input:
    if line != "Hello!":
        output.write(line)

input.close()
output.close()