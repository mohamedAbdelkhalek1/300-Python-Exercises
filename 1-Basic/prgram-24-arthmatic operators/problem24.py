
"""
problem 24:

Write A Python Program To Get Two Number And Operator From The User To Perform Arithmetic Operation


"""


# to get 2 number from the user
# one operator 
# perform arithmetic operations 

a =  int(input("Enter 1st numebr")) # 4
b = int(input("Enter 2nd numebr")) # 7
op = input("Insert a operator to perform operation") # /

if(op == '+'):
    print("Addition of two numebr is = "+str(a+b))
elif(op == '-'):
    print("Subtraction of two numebr is = "+str(a-b))
elif(op == '/'):
    print("Division of two numebr is = "+str(a/b))
elif(op == '*'):
    print("Multiplication of two numebr is = "+str(a*b))
elif(op == '%'):
    print("Mod of two numebr is = "+str(a%b))
else:
    print("Invalid Operator, please one of them as +, -, /, * and %")




# #Another form of
# num1 = int(input("Enter number 1 :"))
# num2 = int(input("Enter number 2 :"))

# operator = input("Enter the operator")

# if operator == "*":
#     print(f"{num1} * {num2} = {num1*num2}")
# elif operator == "+":
#     print(f"{num1} + {num2} = {num1+num2}")
# elif operator == "/":
#     print(f"{num1} / {num2} = {num1/num2}")
# elif operator == "-":
#     print(f"{num1} - {num2} = {num1-num2}")
# elif operator == "%":
#     print(f"{num1} % {num2} = {num1%num2}")
# else:
#     print("InvValid operator")