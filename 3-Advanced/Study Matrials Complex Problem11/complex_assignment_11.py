"""
complex_assignment_7:

Write A Python Program To Get String From User To Display Required Character That Present On Odd Index Number.
Required Character Get From User

"""
user_input = input("Enter a string: ")

print("Characters at odd index positions:", user_input[1::2])



# #another solution
# user_input = input("Enter a string: ")

# odd_characters = ""

# for index, character in enumerate(user_input):
#     if index % 2 != 0:
#         odd_characters += character

# print("Characters at odd index positions:", odd_characters)