"""
assignment 29:

Write A Python Program To Get Number To Check, Whether It Is Positive, Negative Or Equal To Zero 

"""



# get a number 
# check, negative or positve 

num = int(input("Enter a number")) # '5' ->5

if(num > 0):
    print(str(num)+" is the Positive")
elif num == 0:
    print(str(num)+" is Equal To Zero")
else:
    print(str(num)+" is the Negative")