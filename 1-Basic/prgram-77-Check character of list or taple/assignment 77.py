"""
assignment 77:

Write A Python Program To Store 5 Student Name In A List 
And Check If The First Char Of First Student Name Is Equal To Last Student’s First Char

"""

std = []

for i in range(5):
    std.append(input(f"Enter the name of student {i+1} : "))
    
if std[0][0] == std[-1][0]:
    print("The First Char Of First Student Name Is Equal To Last Student’s First Char")
else:
    print("The First Char Of First Student Name Is Not Equal To Last Student’s First Char")