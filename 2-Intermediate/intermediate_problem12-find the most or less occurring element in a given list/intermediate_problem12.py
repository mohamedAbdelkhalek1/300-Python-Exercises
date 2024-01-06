"""
intermediate_problem12:

Write a Python program to find the most occurring element in a given list of numbers.

"""



from statistics import mode
lst = [11,2,3,3,1,1,2,3,4,5,6,7,9]
print(lst)
print(mode(lst))


# #Solve with hash table
# lst = [11,2,3,3,1,1,2,3,4,5,6,7,9]

# hash_table = dict() 
# for e in lst:
#     if e in hash_table.keys():
#         hash_table[e] += 1
#     else:
#         hash_table[e] = 1
        
# max_value = max(list(hash_table.values()))
# most_rep = 0
    
# for k in hash_table.keys():
#     if hash_table[k] == max_value:
#         most_rep = hash_table[k]
        
        
# print("the most occurring element in a given list of numbers is ",most_rep)