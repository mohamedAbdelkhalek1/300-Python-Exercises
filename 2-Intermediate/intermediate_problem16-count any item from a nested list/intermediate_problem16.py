
"""
intermediate_problem16:

Write a Python program to count any item from a nested list.

"""

n_list = [[1,2,3,4],[3,3,4,12]]
print(n_list)
item = int(input("Enter a list item")) # '2'> 2
reuslt = sum(i.count(item) for i in n_list)
print(reuslt)




# # Another solution
# n_list = [[1,2,3,4],[3,3,4,12]]
# print(n_list)
# item = int(input("Enter a list item")) # '2'> 2
# count = 0
# for i in n_list:
#     count += i.count(item)

# print(count)