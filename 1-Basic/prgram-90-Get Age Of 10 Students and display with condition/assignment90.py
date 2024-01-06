"""
assignment 90:

Write A Python Program To Get Name Of Different Students From User And Store In A List.
Condition Is That, System Should Stored The Name Of Student That Start From Char ‘a’ And End At ‘a’ Char 


"""

students = []

for i in range(5):
    name = input("Enter student name only Stored The Name Of Student That Start From Char ‘a’ And End At ‘a’ Char : ")
    if name.startswith("a") and name.endswith("a"):
        students.append(name)

print(students)





# # Another solution more logic
# student_names = []

# while True:
#     name = input("Enter a student name (or 'q' to quit): ")

#     if name.lower() == 'q':
#         break

#     if name.lower().startswith('a') and name.lower().endswith('a'):
#         student_names.append(name)

# print("Student names that start with 'a' and end with 'a':")
# print(student_names)