
"""
problem 72:

Write A Python Program To Shuffle a List Of Different Color Code.

shuffle means print list with random order

"""


# to get color code
# shuffle the color code and display
import random
color_code = []

for i in range(5):
    color_code.append(input("Enter Color Code"))
random.shuffle(color_code)
print(color_code)
