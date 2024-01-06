"""
assignment 74:

Write A Python Program To Find The Second Position Of A Student In A List. And Display Student Marks And Student Name

"""

std_names = []
std_marks = []

for i in range(4):
    std_names.append(input(f"Enter name of student {i+1} : "))
    std_marks.append(int(input(f"Enter marks of student {i+1} : ")))
    

print("2nd Student Marks = "+str(sorted(std_marks[-2])))

print("Total Result of Students = "+str(std_marks))
print("Names  of Students = "+str(std_names))

