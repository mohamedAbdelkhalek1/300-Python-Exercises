"""
assignment 40:

Write Python Program To Get Username From User And Make Sure That Username Should Contain Alphanumeric Character
AND Username Length Should Not Be Less Than Or Equal To 8 

"""

def check_user(u):
    if len(u) > 8:
       if(u.isalnum()):
          print("Your Username "+str(u)+" is Okay")
       else:
          print("Sorry, use only alpha or numaric without whitespace")
    else:
        print("Sorry, Username Length Should Be more Than 8 ")
        
user = input("Enter username ")
check_user(user)