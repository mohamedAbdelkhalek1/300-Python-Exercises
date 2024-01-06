"""
intermediate_problem31:

Write a Python Program to Create a dictionary that displays those values that have vowel characters.

"""


d = {1:"Rd",14:"Blue",2:"Yellow",6:"Black",9:"JFR"}
print(d)
# a e o i u 
for value in d.values():
    if 'a' in value or 'e' in value or 'o' in value or 'i' in value or 'u' in value:
        print(value)

