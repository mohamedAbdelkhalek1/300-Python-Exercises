"""
complex_assignment_36:

Write a Python Program To Get a Sentence From User And Also Get a Char Or Set Of Char To Check At Start of Sentence.

"""
import re

sent = input("Enter a sentence")
char = input("Enter a char or set of char")

x = re.search("^"+char, sent)

if x:
    print("Matching....")
else:
    print("Not Matching")