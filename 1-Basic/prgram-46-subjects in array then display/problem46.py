
"""

problem 46:

Write A Python Program To Get 5 Subject Marks, Store Them Into Array, And Also Get Student Name. Find Total And Display Each Subjects Marks.

Expected result:

Hi username!
Your marks is ……
See your all subject marks
English = …
AI = …
Physics = …
Computer = …
Math= …

"""


# to get username
# 5 subject marks 
# dispaly total, and every subject marks ind:
import array as arr

user = input("Enter your name ")
a = arr.array('i',[])
print("Enter subject marks in this order English, AI, Physics, Computer, Math")

total = 0

for i in range(5): #0, 1 , 2, 3, 4
    a.append(int(input("Enter subject marks")))
    total += a[i]




print("Hi, "+user+"!")
print("Your marks is"+str(total))
print("See your all subject marks")
print("English = "+str(a[0]))
print("AI = "+str(a[1]))
print("Physics = "+str(a[2]))
print("Computer = "+str(a[3]))
print("Math = "+str(a[4]))
