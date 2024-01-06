"""
assignment 86:

Write A Python Program To Get A Sentence From A User, User Should Able To Remove Any Character From A String

"""
s = input("Enter a string : ")
print(s)
ch = input("Enter char or set of char to remove : ")
new_string = s.replace(ch, "")
print("String after remove : ",new_string)