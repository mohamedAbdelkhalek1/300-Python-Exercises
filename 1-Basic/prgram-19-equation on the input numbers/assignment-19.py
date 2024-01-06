"""
assignment 19:

Write A Python Program To Get 4 Number From User And Put In The Following Equation:
d+a+2ab/d(4c+10)


"""



# to get 4 num from user
# put in to the equaiton 
# dispaly result to user

a = int(input("Enter a number"))
b = int(input("Enter b number"))
c = int(input("Enter c number"))
d = int(input("Enter d number"))

result = d+a+2*a*b/d(4*c+10)
print("Result is = "+str(result))