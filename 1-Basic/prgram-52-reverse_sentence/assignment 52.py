"""
assignment 52:

Write A Python Program To Get A Sentence From The User, 
To Reverse That Sentence And Enclose In Double Quotations And Put A Full Stop At The End Of Sentence


"""


def reverse_sentence(sentence):
    reversed_sentence = sentence[::-1]  # Reverse the sentence using slicing
    reversed_sentence = '"' + reversed_sentence + '"'  # Enclose in double quotations
    reversed_sentence += '.'  # Add a full stop at the end
    return reversed_sentence

# Prompt the user for a sentence
sentence = input("Enter a sentence: ")

# Reverse the sentence, enclose in double quotations, and add a full stop
reversed_sentence = reverse_sentence(sentence)

# Print the reversed sentence
print("Reversed Sentence:", reversed_sentence)



# # another solution
# st = input("Enter the sentance to reverse :  ")
# reverse_st = ""

# for i in st:
#     reverse_st += i

# print(f"Reverse sentance \" {reverse_st} . \"")