"""
problem 87:

Write A Python Program To Get A Sentence From User, The System Should Display Only Ten Character Maximum

"""

# get sentence from user
# display only 10 char

s = input("Enter a sentence")
print("Your Sentence is "+s)
print(s[slice(0, 11)]) # 0 to 11-1


# #Another solution
# print(s[0:11])
