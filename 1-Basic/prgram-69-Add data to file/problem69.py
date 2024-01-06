
"""
problem 69:

Write A Python Program To Create A File And Write User Name, And Age In That File

"""

# create file
# get name and age 
# write on the file

# file = open("jafri.txt","w+")
# name = input("Enter your name")
# age = input("Enter your age")
# file.write("Your name is "+str(name))
# file.write("Your age is "+str(age))
# file.close()


file = open("E:/bulding/python_exercises/1-Basic/prgram-69-/data.txt","w")

file.write("Name : mohammed \n")
file.write("Age : 22 \n")
file.close()

# for i in file:
#     print(i)