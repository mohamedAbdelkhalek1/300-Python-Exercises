"""
assignment 64:

Write A Python Program To Find Scholarship For Students In Admission In A College On The Basis Of Student Marks, Using Function

Criteria To Follow
Marks Equal To 11000 	Free Education
Marks > 1000	 	80%  Monthly Fees Deduction
Marks > 900		60%  Monthly Fees Deduction
Marks > 800		40%  Monthly Fees Deduction
Marks > 700		30%  Monthly Fees Deduction
Marks > 600		There Is No Scholarship 

"""

def find_scholarship(marks):
    if(marks == 1100):
       print("Free Education")
    elif (marks > 1000):
       print("80%  Monthly Fees Deduction")
    elif (marks > 900):
       print("60%  Monthly Fees Deduction")
    elif (marks > 800):
       print("40%  Monthly Fees Deduction")
    elif (marks > 700):
       print("30%  Monthly Fees Deduction")  
    elif (marks > 600):
       print("There Is No Scholarship")
    else:
       print("Enter valid number")
       
       
marks = int(input("Enter your marks"))

find_scholarship(marks)