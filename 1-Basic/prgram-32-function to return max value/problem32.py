"""
problem 32:

Write A Python Program To Get Two Number From The User , Pass To Function And Find Maximum


"""


# to get 2 number 
# pass to function 
# max

def max_num(n1, n2):
    if(n1 > n2):
        return n1
    else:
        return n2



num1 = int(input("Enter a numebr 1 : "))
num2 = int(input("Enter b numebr 2 : "))



print("Muximum number is : ",max(num1,num2))