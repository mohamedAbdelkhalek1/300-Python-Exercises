
"""
problem 40:

Write Python Program To Get A Username From The User That Should Have Alphanumeric Characters,
Then Pass That Username To Function As Parameter, To Display That Username


"""




# to get username 
# to pass to the function
# to check alpha numaric char
# display to user

user = input("Enter username ")
def check_user(u):
    if(u.isalnum()):
        print("Your Username "+str(u)+" is Okay")
    else:
        print("Sorry, use only alpha or numaric without whitespace")
check_user(user)