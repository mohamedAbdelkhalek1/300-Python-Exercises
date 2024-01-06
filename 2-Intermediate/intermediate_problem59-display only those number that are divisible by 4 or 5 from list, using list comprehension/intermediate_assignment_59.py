"""
intermediate_assignment_59:

Write a Python Numpy Program to Find the number of occurrences of a sequence in an array.

"""
import numpy as np


lst = [1,1,2,2,3,4,5,1,5,6]

arr = np.array(lst)

occurrence_dic = {}

for element in arr:
    if element in occurrence_dic:
        occurrence_dic[element] += 1
    else:
        occurrence_dic[element] = 1
        
for element , occurrence in occurrence_dic.items():
    print(f"{element} have occerrences of {occurrence}")