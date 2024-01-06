"""
intermediate_assignment_25:

Write a Python program to get the total length of all keys of a dictionary with string keys. 

"""


d = {"color1":"Red","color2":"Blue","color3":"Yellow","color4":"Black","color5":"Green"}
print(d)
a = 0
for i in d.values():
    a  += len(i)

print(a)