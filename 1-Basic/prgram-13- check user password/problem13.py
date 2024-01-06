
"""
problem 13:

Write Python Program To Get Password From User And Make Sure That Password Should Contain Number And Alphabetic only



"""



# to check user password

pwd = input("Enter your password")

if pwd.isalnum():
    print("Your password is okay, that is "+pwd)
else:
    print("Sorry, we did not allow white space and special char in your password that is "+pwd)



