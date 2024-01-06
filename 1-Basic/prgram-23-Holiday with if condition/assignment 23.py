"""
assignment 23:

Write a Python program get name of week and show “Holiday” if user input Sunday or Friday

"""


day = input("Enter name of day : ")

if day in ["Sunday","sunday","Sun","sun","Friday","friday","Fri","fri"] :
    print("Holiday")
else:
    print("It is not Holiday")