
"""
assignment 92:

Write A Python Program To Find Celling And Floor Of A Number

Ceiling Of A Number : means next That , rounding the number to the next number as : 5.2 --> 6

floor Of A Number : means That is, rounding the number to the number before it as : 5.2 --> 5 , 5.7 --> 5

"""

# to get number
# find ceiling of number

import math
num = float(input("Enter a number"))
print(math.ceil(num))
print(math.floor(num))