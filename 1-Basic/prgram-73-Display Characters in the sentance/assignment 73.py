"""
assignment 73:

Write A Python Program To Get A Sentence From User, To Count Specific Word In A Sentence

"""


s = input("Enter the sentance")

word = input("Enter a specific word to count it in the sentance")

word_count = s.count(word)

print(f"The word {word} in the sentance : {word_count} times")