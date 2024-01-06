"""
problem 31:

Write A Python Program To Get Marks Of Student To Find Its Grade 
Using This Criteria
>=95 Show A+ Grade
>=80 Show A Grade
>=70 Show B Grade
>=60 Show C Grade
Lower Than 60, Will Be Fail Consider


"""




# # to get students marks
# # to find grade
# # >=95 A+
# # >=80 A
# # >=70 B
# # >=60 C
# # <60 Fail

# marks = int(input("Enter your marks to find Grade"))
# # '90' -> 90
# if(marks >= 95):
#     print("Grade is A+")

# elif(marks >=80):
#     print("Grade is A")

# elif(marks >=70):
#     print("Grade is B")

# elif(marks >=60):
#     print("Grade is C") 
# else:
#     print("Fail")






marks = int(input("Enter the mark : "))

if marks<0 or marks>100:
    print("Invalid marks")
    
elif marks>=95:
    print ("Grade is A+")
elif marks>=80:
    print ("Grade is A")
elif marks>=70:
    print ("Grade is B")
elif marks>=60:
    print ("Grade is C")
else:
    print("Fail")
