"""
assignment_problem_8:

Write A Python Program To Generate A Strong Password, Password Length Should Be Decided By User. 

"""

import random 

import string

pass_len = int(input("Enter the length of needed password"))

txt = string.ascii_letters + string.digits + string.punctuation + " "

random_txt = list(txt)

random.shuffle(random_txt)

pwd = random_txt[:pass_len]

print(''.join(pwd))

