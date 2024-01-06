"""
problem 19:

Write A Python Program To Get 3 Number From User And Put In The Following Equation:
	a+b+ca/b(2a + 3b)


"""



# to get 3 num from user
# put in to the equaiton 
# dispaly result to user

a = int(input("Enter a number"))
b = int(input("Enter b number"))
c = int(input("Enter c number"))

result = (a+b+c)*(a/b)*(2*a+3*b)
print("Result is = "+str(result))