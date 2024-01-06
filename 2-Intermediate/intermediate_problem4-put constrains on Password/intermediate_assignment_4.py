"""
intermediate_assignment_4:

Write A Python Program To Get Password From The User That Contain Alpha Numeric, Special Characters, 
And More Than 8 And Less Than 20 Characters And Restrict User If User Include Uppercase Letter And Space

"""

pwd = input("Enter your password : ")

if not pwd.isalnum() and pwd.islower() and " " not in pwd :
    if(len(pwd) > 8 and len(pwd) < 20):
        print("Your password is okay")
    else:
        print("Sorry, your password is not correct, you have to enter pwd, that should be more than 8 and less than 20 char")
else:
    print("Sorry, include Alpha Numeric, Special Characters in your password and not Include Uppercase Letter And Space")

