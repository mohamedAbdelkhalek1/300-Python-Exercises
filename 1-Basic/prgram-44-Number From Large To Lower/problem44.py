
"""
problem 44:

Write A Python Program To Get Large Number As Starting And Lower Number As Ending Number, Display That Number From Large To Lower.

As User Input 10 As Large Number And 5 As Lower Number, Then It Should Display As:
10,9,8,7,6,5

"""





# to get starting no that is larger
# to get ending no that is lower
# generate no from starting to ending

s = int(input("Enter a starting no, that is larger"))# 10
e = int(input("Enter a ending no that is lower"))   # 1
for i in range(s, e-1, -1):      #third index in range() function refere to step
    print(i)
    # 10, 9, 8, 7.... 1