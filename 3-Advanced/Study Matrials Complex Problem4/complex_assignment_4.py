"""
complex_assignment_4:

Write A Python Program To Convert Binary Into Decimal Number Using Recursion

"""
def binary_to_decimal(binary):
    if len(binary) == 0:
        return 0
    else:
        return int(binary[0]) * (2 ** (len(binary) - 1)) + binary_to_decimal(binary[1:])


binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)
print("Decimal equivalent:", decimal_number)


# def bin_to_dic(bin_num,x=0):
#     if bin_num ==0:
#         return 0
#     add_value = bin_num%10
#     bin_num = int(bin_num/10)
#     return add_value* 2**x + bin_num(bin_num,x+1)

# binary = int(input("Enter a binary number : "))
# print("Dicimal = ",bin_to_dic(binary))
