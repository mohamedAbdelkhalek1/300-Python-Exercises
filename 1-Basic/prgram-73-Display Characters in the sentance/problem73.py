"""
problem 73:

Write A Python Program To Get A Sentence From User, To Display Last Character Of That Sentence AND Also Display All The Characters One By One. 

"""


s = input("Enter a sentence")
print("Your sentence is = "+s)
print("Last Char "+s[-1]) # How are you

for i in s:
    print(i)