"""
complex_assignment_70:

Write a Python Program to take a string from user to search in two file

"""
para1 = input("Enter a paragraph 1 : ")
para2 = input("Enter a paragraph 2 : ")
# I am faisal zamir, working on teaching programming languages, web designing, web development everything...
file1 = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem70/mysearchfile_1.txt","r+")
file2 = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem70/mysearchfile_2.txt","r+")
file1.write(para1)
file2.write(para2)

word = input("Enter a word to search in file : ")

lines1 = file1.readlines()
lines2 = file2.readlines()

find = 0

for line in lines1:
    if line.find(word) != -1:
        find = 1

        
if find !=1:
    for line in lines2:
        if line.find(word) != -1:
            find = 2
            
if find == 1:
    print("Word is existed in file 1")
elif find == 2:
    print("Word is existed in file 2")
else:
    print("No word in any file")


file1.close()
file2.close()
