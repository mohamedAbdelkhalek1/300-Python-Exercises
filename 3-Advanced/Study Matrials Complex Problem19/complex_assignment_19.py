"""
complex_assignment_19:

Write A Python Program To Get File Name From User If File Name Have Space Then Replace Space With ‘Dot’ Symbol

"""


file = input("Enter a file name : ") # my file
flag = "No"
for i in file:
    if i.isspace():
        flag = "Yes"

if flag == "Yes":
    print("File contain space")
    new_file = file.replace(" ", ".") 
    print("New file : ",new_file)
else:
    print("File name is "+file+" there is no space")