
"""
problem 86:

Write A Python Program To Search Any Character (or Set of Character) From a String.

"""

s = input("Enter a string")
print(s)
ch = input("Enter char or set of char")
if ch in s:
    print("Yes")
else:
    print("No")