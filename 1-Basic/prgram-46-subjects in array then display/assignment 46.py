"""
assignment 46:

Write A Python Program To Get 5 Subject Marks, Store Them Into Array, And Also Get Student Name.
Find Total And Average And Display Each Subjects Marks.

Expected result:
Hi username and your class is ---------
Your marks is ……
See your all subject marks
English = …
AI = …
Physics = …
Computer = …
Math= …
Your marks average is = ….

"""
from array import array 

subjects = ["English","AI","Physics","Computer","Math"]
user = input("Enter your name: ")

marks = array("i",[])
total = 0
for i in range(5):
    marks.append(int(input(f"Enter {subjects[i]} marks : ")))
    total += marks[i]
    
print("Hi, "+user+"!")
print("Your marks is"+str(total))
print("Your Average is"+str(total/5))
print("See your all subject marks")
print("English = "+str(marks[0]))
print("AI = "+str(marks[1]))
print("Physics = "+str(marks[2]))
print("Computer = "+str(marks[3]))
print("Math = "+str(marks[4]))
