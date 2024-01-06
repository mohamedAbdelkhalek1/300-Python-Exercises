"""
intermediate_assignment_5 :

Write A Python Program To Get 10 Name Of The Students And Display Them On The Screen
And User Able To Update Any Student On Run Time

"""

lst = []
for i in range(2):
    s = input("Enter Student Name : ")
    lst.append(s)
print("Student List"+str(lst))
std_1 = input("Enter Stduent name, you wnat to update : ")
std_2 = input("Enter Stduent name, you wnat to updated with : ")
lst[lst.index(std_1)] = std_2
print("Student List"+str(lst))
