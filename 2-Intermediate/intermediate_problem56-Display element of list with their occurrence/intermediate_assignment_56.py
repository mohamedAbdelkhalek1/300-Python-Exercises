"""
intermediate_assignment_56:

Write a Python Program to display element of list with their occurrence using another method.

"""
lst = [1,1,2,2,3,4,5,1,5,6]
print(lst)

occurrence_dic = {}

for element in lst:
    if element in occurrence_dic:
        occurrence_dic[element] += 1
    else:
        occurrence_dic[element] = 1
        
for element , occurrence in occurrence_dic.items():
    print(f"{element} have occerrences of {occurrence}")