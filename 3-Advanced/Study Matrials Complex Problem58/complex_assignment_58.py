"""
complex_assignment_58:

Write a Python Program to make List of students to a text file

"""
myfile = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem58/filelist.txt","w")
lst = ["Ali", "Sara", "Mohammed"]
for i in lst:
    myfile.write(str(i)+"\n")

myfile.close()