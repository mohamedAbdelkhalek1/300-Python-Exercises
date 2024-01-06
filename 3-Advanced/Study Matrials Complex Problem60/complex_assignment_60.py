"""
complex_assignment_60:

Write a Python Program to read specific lines from a File. More than one line should be display. 

"""
file = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem60/input.txt","r")
r = file.readlines()

n = int(input("How many lines do you want to print? "))
for i in range(n):
    line = int(input(f"Enter a line number {i+1} : ")) 
    print(r[line-1])
 