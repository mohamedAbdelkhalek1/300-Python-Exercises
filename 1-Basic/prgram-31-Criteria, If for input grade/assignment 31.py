"""
assignment 31:

Write A Python Program To Get Scale From Employer And Then Display Salary According To Employer Scale
Using This Criteria, If:
Scale Is 9, display 10,000
Scale Is 12 , display 20,000
Scale Is 15 , display 40,000
Scale Is 18 , display 50,000
Scale Is 20 , display 70,000


"""


scale = int(input("Enter the scale : "))

if scale<0 or scale>20:
    print("Invalid scale")
    
elif scale==9:
    print ("Salary is 10,000")
elif scale==12:
    print ("Salary is 20,000")
elif scale==15:
    print ("Salary is 40,000")
elif scale==18:
    print ("Salary is 50,000")
elif scale==20:
    print ("Salary is 70,000")
else:
    print("Fail")
