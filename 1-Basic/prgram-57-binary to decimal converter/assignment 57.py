"""
assignment 57:

Write A Python Program To make binary to decimal conversion calculator 

"""

def binary_to_decimal(bin):
    decimal = 0
    for i in range(len(bin)):
        index = (i+1)*-1
        decimal += ( int(bin[index]) * 2**i)
    return decimal

print(binary_to_decimal("101"))   #5




# # another solution with int()
# binary_number = input("Enter a binary number: ")
# decimal_number = int(binary_number, 2)
# print("Decimal equivalent: ", decimal_number)
