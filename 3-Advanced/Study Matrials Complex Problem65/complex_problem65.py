"""
complex_problem65:

Write a Python Program to get a word from user that not contain any vowel char. That specific word should be save into a file.

"""

word = input("Enter a word")
user_word = word.lower()
flg = "no"
# a e i o u
for i in user_word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        flg = "yes"


file = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem65/vowlfile.txt","w")
if flg == "yes":
    print("Your word is "+user_word)
else:
    file.write(user_word)
    file.close()
    print("It did not contian any vowel that is "+user_word)

