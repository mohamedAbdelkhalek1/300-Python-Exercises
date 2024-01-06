"""
intermediate_assignment_6:

Write a Python Program To Find Total Length Of Values And Keys In a Dictionary

"""
dict = {"Name":"Faisal","Age":30,"cors":"Python"}

total_length = 0

for key,value in dict.items():
    total_length += len(str(key)) + len(str(value))
    
print(f"Total Length Of Values And Keys In a Dictionary = {total_length}")


