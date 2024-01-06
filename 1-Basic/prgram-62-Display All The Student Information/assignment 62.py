"""
assignment 62:

Write A Python Program To Get Different Information Of Students From User And Display All The Student Information In This Order.
And After Displaying, Update User CNIC, Age And Contact, Then Display Updated Result.
Name			---------
Father Name 		---------
CNIC			---------
Age 			---------
Contact	 		---------

"""

name = input("Enter your full name")
f_name = input("Enter your father  name")
cnic = input("Enter your CNIC")
age = input("Enter your age")
contact = input("Enter your contact")

print("This is a student informaiton that we get from user")
print("Name \t\t "+name)
print("Father Name \t\t "+f_name)
print("CNIC \t\t "+cnic)
print("Age \t\t "+age)
print("Contact \t\t "+contact)


cnic = input("Enter your CNIC again to update")

print("This is a student informaiton that we get from user after updating")
print("Name \t\t "+name)
print("Father Name \t\t "+f_name)
print("CNIC \t\t "+cnic)
print("Age \t\t "+age)
print("Contact \t\t "+contact)
