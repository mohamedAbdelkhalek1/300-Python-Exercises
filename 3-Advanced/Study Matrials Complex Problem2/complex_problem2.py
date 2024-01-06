"""
complex_problem2:

Write A Python Program To Get A Paragraph From User, To Find(total Char, without space total char, Total Words And Spaces)

"""


# total char with and without space
# total words
# total spaces
sentence = input("Enter a sentence")
total_char_with_space = len(sentence)

spaces = 0
for i in range(total_char_with_space):
    if sentence[i] == " ":
        spaces += 1
print(spaces)
total_words = spaces + 1

total_char_without_spaces = total_char_with_space - spaces

print("Total Char with space " +str(total_char_with_space))
print("Total Char without space " +str(total_char_without_spaces))
print("Total words " +str(total_words))
print("Total spaces " +str(spaces))