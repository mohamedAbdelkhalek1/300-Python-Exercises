"""
assignmen 70:

Write A Python Program To Get Student Identity, System Should Help To Avoid Duplicate Identity Insertion.

"""


std_id = []

for i in range(4):
    std = input("Enter student name : ")
    if std_id.count(std) < 1:
        std_id.append(std)
    else:
        print("Sorry, Duplication of Student")
        
print(std_id)


