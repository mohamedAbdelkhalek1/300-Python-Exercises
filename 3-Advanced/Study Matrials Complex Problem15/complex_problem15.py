"""
complex_problem15:

Write a Python Program To Find Keyword Density In  Article 

"""


para = input("Enter a paragraph...")
word = input("Enter a word or keywrod to find density")
sp = 0
for i in para:
    if i == " ":
        sp += 1
total_words = sp + 1
print("Total Words = "+str(total_words))
user_word = para.count(word)
print("User Word occurences ="+str(user_word))

keyword_density = (user_word / total_words) * 100
print("Keyword Density = "+str(keyword_density)+"%")
