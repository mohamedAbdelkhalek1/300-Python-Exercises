"""
assignment 88:

Write A Python Program To Get A Number From User, The System Should Auto Decrement To That Number.
Half Of User Entered Number Should Be Decremented


"""

num = int(input("Enter a number"))
# find half of that number
half_num = num/2
print("Half of "+str(num)+ "is "+str(half_num))
decrement = num - half_num
print("Result is "+str(decrement))