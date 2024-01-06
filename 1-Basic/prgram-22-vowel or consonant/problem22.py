"""
problem 22:

Write A Python Program To Check Alpha Character, Whether Vowel Or Consonant.


"""





# to get char from user 
# check , vowel or not

char = input("Enter a char")
# a e i o u or = ||
if((char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u')):
    print("It is vowel")
else:
    print("It is cons..")
    





# #another solution
# char = input("Enter the character")
# if len(char) == 1:
#     if char in ['E','e','I','i','A','a','U','u','O','o']:
#         print("Vowel character")
#     else:
#         print("Consonant character")
# else:
#     print("please enter one character")