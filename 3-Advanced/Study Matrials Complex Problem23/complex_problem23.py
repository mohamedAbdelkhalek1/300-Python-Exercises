"""
complex_problem23:

Write A Python Program To Generate OTP On User Request

"""

import random
import string

req = input("Would you want to generate OTP y/n")

if req == "y":
    l = int(input("Enter the length of OTP you want"))
    otp = "".join(random.choices(string.digits + string.ascii_uppercase, k = l))
    print(otp)
else:
    print("Ok, Not at all")