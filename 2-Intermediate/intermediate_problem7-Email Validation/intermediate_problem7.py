
"""
intermediate_problem7:

Write A Python Program To Get An Email From The User And Make Sure That It Is an Email In Proper Format Having @ Symbol And .

"""

import re

email = input("Enter a email ")
pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#another way of pattern
# pattern = r"^[A-z0-9_\.]+@[A-z0-9_\.]+\.(com|net|org)"
match  = re.search(pattern, email)

if match :
    print("Email is valid")
else:
    print("Email is invalid")