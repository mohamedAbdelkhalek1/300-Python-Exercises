"""
problem 61:

Write A Python Program To Get Memory In GB Then Convert GB In To Bytes

"""


# to get memory in gb
# convert to byt

gb  = float(input("Enter memory in GB")) # 2
# 1GB =1024*1024*1024 = 1073741824 Bytes

memory_in_byte = 1073741824 * gb
print("GB is converted to Bytes "+str(memory_in_byte))