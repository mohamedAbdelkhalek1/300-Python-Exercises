"""
complex_assignment_2:

Write A Python Program To Get A Paragraph From User, To Find(total Char, Total Words, Total Vowel Char And Spaces)

"""

# total char with and without space
# total words
# total spaces
#Total Vowel Char
sentence = input("Enter a sentence")
total_char_with_space = len(sentence)

spaces = 0
vowel = 0
for i in range(total_char_with_space):
    if sentence[i] == " ":
        spaces += 1
    if sentence[i] in "AaEeUuIiOo":
        vowel += 1
total_words = spaces + 1

total_char_without_spaces = total_char_with_space - spaces

print("Total Char with space " +str(total_char_with_space))
print("Total Char without space " +str(total_char_without_spaces))
print("Total words " +str(total_words))
print("Total spaces " +str(spaces))
print("Total vowels " +str(vowel))