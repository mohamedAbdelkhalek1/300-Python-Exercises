"""
problem 56:

Write A Python Program To  Make a percentage calculator. 

"""


# get amount
# cal per from that amount

amount = int(input("Enter amount")) #100
per = int(input("Enter percentage, you wan to get")) # 20
percentage = (per*amount)/100

print("Your amount is = "+str(amount))
print("Your percentage from "+str(amount)+ "is "+str(percentage))


