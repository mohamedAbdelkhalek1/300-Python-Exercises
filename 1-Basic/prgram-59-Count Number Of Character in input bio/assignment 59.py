"""
assignment 59:

Write A Python Program To Get A Bio From A User And Count Specific word in a User Bio.

"""


bio = input("Enter the Bio : ")
word = input("Enter the spacific word to count : ")

word_count = bio.count(word)

print(f" number of {word} in the Bio = {word_count}")