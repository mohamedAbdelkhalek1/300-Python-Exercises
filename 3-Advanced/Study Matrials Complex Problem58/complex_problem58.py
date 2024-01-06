"""
complex_problem58:

Write a Python Program to make dictionary to a text file.

"""

myfile = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem58/filedict.txt","w")
dict = {1:"red",2:"blue",3:"yellow",4:"white"}

for k,v in dict.items():
    myfile.write(str(k)+" : "+str(v)+"\n")

myfile.close()