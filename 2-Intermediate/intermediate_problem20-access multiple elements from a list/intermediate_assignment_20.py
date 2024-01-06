"""
intermediate_assignment_20:

Write a Python program to access multiple elements from a tuple. Starting index and ending index provided by user.    


"""

tpl = (1,2,3,4,56,6,7,8,9,10)
print(tpl)
s = int(input("Enter starting item position")) # 0
e = int(input("Enter Ending item position")) #  5
ending = e+1
print(tpl[s:ending])