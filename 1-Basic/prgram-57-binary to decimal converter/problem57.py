
"""
problem 57:

Write A Python Program To Make a decimal to binary conversion calculator.

"""
def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


num = 5
binary = decimal_to_binary(num)
print(binary)






#Another solution
# # decimal_num = int(input("Enter the dicimal number to convert to binary"))
# print(bin(5))

