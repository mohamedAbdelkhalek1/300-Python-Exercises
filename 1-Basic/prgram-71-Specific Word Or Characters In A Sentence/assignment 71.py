"""
assignment 71:

Write A Python Program To Find Occurrence Of A Specific Word Or Characters In A Sentence, Then Replace With Another Word Or Characters

"""

s = input("Enter a sentence ")
w_c_1 = input("Enter a char or word, you want to Find ")
w_c_2 = input("Enter a char or word, you want to Replace with it ")


print("Your sentence "+"\'"+s+"\'")
print("Your word or char you want to replace it is "+"\""+w_c_1+"\"")
print("Your word or char you want to replace with it is "+"\""+w_c_2+"\"")
print("Your sentence become : "+"\'"+s.replace(w_c_1, w_c_2)+"\'")