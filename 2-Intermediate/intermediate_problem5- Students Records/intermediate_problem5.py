"""
intermediate_problem5:

Write A Python Program To Store Students Records, User Will Be Able To Delete Any Student From A Record On Run Time

"""


lst = []
for i in range(10):
    s = input("Enter Student Name")
    lst.append(s)
print("Student List"+str(lst))
std_name = input("Enter Stduent name, you wnat to delete")
lst.remove(std_name)
print("Student List"+str(lst))

