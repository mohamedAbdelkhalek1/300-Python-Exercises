
"""
intermediate_problem17:

Write a Python Program To Get a word from a user.
The word should contain lower and uppercase both. Then convert lower to upper and upper to lower.

"""


# import re
# word = input("Enter a word")
# x = re.search('[a-z]+[A-Z]+', word) # faISAL
# lst = []
# if x:
#     for i in word:
#         if i.isupper():
#             new_char = i.lower()
#             lst.append(new_char)
#         if i.islower():
#             new_char = i.upper()
#             lst.append(new_char)

# else:
#     print("NO")

# print(lst)
# converted_word = "".join(lst)
# print(converted_word)


#Another solution
import re

word = "MoBeBo"

pattern = r"[A-Z]*[a-z]+[a-z]*[A-z]+"  

search = re.search(pattern, word)

if search:
    print("Valid Word")
    print("After convertion : ",word.swapcase())
    # print(search.group())
else:
    print("Invalid Word")