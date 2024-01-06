"""
assignment 32:

Write A Python Program To Get Two Number From The User , Pass To Function And Find Minimum

"""


# to get 2 number 
# pass to function 
# min

def min_num(n1, n2):
    if(n1 > n2):
        return n1
    else:
        return n2



num1 = int(input("Enter a numebr 1 : "))
num2 = int(input("Enter b numebr 2 : "))



print("Minimum number is : ",min(num1,num2))