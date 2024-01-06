"""
complex_problem68:

Write A Python Program To Get a number from user and display table of that number in a file.
And find product of all result that come from table.

"""

num = int(input("Enter a number : "))

my_file = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem68/file.txt","w")

result = 1

my_file.write("Table of "+str(num)+"\n")
for i in range(1,13):
    pro = num * i
    result *= pro
    txt = str(num)+" x "+str(i)+" = "+str(pro)+"\n"
    my_file.write(txt)
    
my_file.write("product of all results = "+str(result))

my_file.close()