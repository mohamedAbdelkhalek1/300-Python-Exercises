
"""
assignment 13:

Write Python Program To Get Password From User And Make Sure That Password Should Contain Number And Alphabetic AND Password Length Should Not Be Greater Than Or Equal To 8 




"""



# to check user password

pwd = input("Enter your password")

if pwd.isalnum():
    if len(pwd) < 8:
       print("Your password is okay, that is "+pwd)
    else:
        print("Sorry, Password Length Should Not Be Greater Than Or Equal To 8 that is "+pwd)
else:
    print("Sorry, we did not allow white space and special char in your password that is "+pwd)



