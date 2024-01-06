"""
intermediate_assignment_1:

Write A Python Program To Check Extension Of A File, If File Extension Is “.mp3” Then Display A Message. “This File Is Not Allowed”

"""

import os

file = input("Enter the file name with extention")

file_name , file_extention = os.path.splitext(file)

if file_extention == ".mp3" :
    print("This File Is Not Allowed")
else:
    print("Done")