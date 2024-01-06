"""
assignment 26:

Write A Python Program To Check A Number, Whether It Is Even Or Odd Number And Then Find That Number Square


"""

num = int(input("Enter a number"))
if (num%2 == 0):# 10, 17%2->1
    print("Number is even")
else:
    print("Number is odd")

print(f"{num} square = {num**2}")