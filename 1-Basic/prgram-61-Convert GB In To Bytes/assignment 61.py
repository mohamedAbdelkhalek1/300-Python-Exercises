"""
assignment 61:

Write A Python Program To Get Memory In Bytes Then Convert Bytes In To GB

"""

# to get memory in byt 
# convert to gb

byt  = float(input("Enter memory in Bytes")) 
# 1GB =1024*1024*1024 = 1073741824 Bytes

memory_in_byte = byt / 1073741824 
print(" Bytes is converted to GB "+str(memory_in_byte))