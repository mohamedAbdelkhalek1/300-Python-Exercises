
"""
problem 52:

Write A Python Program To Get A Sentence From The User, To Reverse That Sentence

"""




# to get sentence/word to reverse
# display to user

st = input("Enter a sentece to reverse")  #jafri
reverse_st = ""
for i in st:
    reverse_st = i + reverse_st
print(reverse_st)     