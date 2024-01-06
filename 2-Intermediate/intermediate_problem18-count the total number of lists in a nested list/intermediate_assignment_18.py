"""
intermediate_assignment_18:

Write a Python program to access element from a nested list.

"""

ne_list = [1,2,3,[2,2],["Jafri","Faisal"],[1.2,0.4]]

for i in ne_list:
    if type(i) == list:
       for j in i:
        print(j)