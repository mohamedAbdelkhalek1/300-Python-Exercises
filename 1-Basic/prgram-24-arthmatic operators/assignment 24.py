"""
assignment 24:

Write a Python program to get two number and operator from the user to perform arithmetic operation. 
And if user provide operator other than arithmetic then restrict user. Using Function


"""
def perform_arithmetic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None
    

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
operator = input("Enter the operator : ")

result = int(perform_arithmetic_operation(num1, num2,operator))

if result == None:
    print("Invalid operator. Please enter a valid arithmetic operator.")
else:
    print("Result: ", result)

