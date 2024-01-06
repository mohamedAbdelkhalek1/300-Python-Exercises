"""
intermediate_assignment_16:

Write a Python program to print a list from a nested list which have lowest number.

"""

n_list = [[1,2,3,4],[3,3,4,12],[5,0,6,7,14]]

lowest = n_list[0][0]

for i in n_list:
    low = min(i)
    if low < lowest:
        lowest = low
  
print("Minimum Value = ",lowest)   
print("And in list : ")           
for i in n_list:
    if lowest in i:
        print(i)
