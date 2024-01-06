"""
assignment 22:

Write a Python program to check alpha character, whether vowel or consonant. And also display “it is number”, if user give any number.


"""


#another solution
char = input("Enter the character")
if len(char) == 1:
    if char in ['E','e','I','i','A','a','U','u','O','o']:
        print("Vowel character")
        
    elif char.isnumeric():
        print("Number : ",char)
    else:
        print("Consonant character")
else:
    print("please enter one character")