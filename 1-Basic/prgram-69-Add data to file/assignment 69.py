"""
assignment 69:

Write A Python Program To Read A Existing File And  Get Two Number From The User, Add them And Display Result To Existing File

"""

file = open("data.txt" , "a")
num1 = input("Enter number 1 to insert to the file : ")
num2 = input("Enter number 2 to insert to the file : ")

file.write(f"The sum of {num1} and {num2} is {num1+num2}\n")

file.close()
