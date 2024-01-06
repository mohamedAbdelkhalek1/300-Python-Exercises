"""
intermediate_assignment_12:

Write a Python program to find less occurring element in a given list of numbers.

"""

lst = [11,11,17,2,3,3,1,1,2,3,4,5,6,7,9]

less_count = lst.count(11)
less_value = 11

for i in lst:
    if lst.count(i) < less_count:
        less_count = lst.count(i)
        less_value = i
        
print("less occurring element in a given list of numbers is : ",less_value)

# #Solve with hash table
# lst = [11,2,3,3,1,1,2,3,4,5,6,7,9]

# hash_table = dict() 
# for e in lst:
#     if e in hash_table.keys():
#         hash_table[e] += 1
#     else:
#         hash_table[e] = 1
        
# min_value = min(list(hash_table.values()))
# less_rep = 0
    
# for k in hash_table.keys():
#     if hash_table[k] == min_value:
#         less_rep = hash_table[k]
        
        
# print("the less occurring element in a given list of numbers is ",less_rep)