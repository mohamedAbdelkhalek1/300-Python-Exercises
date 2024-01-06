"""
intermediate_assignment_48:

Write a Python Program to Create a list from an existing dictionary that counts numbers less than 20 greater than 5

"""

numbers_dict = {'A': 10, 'B': 15, 'C': 3, 'D': 25, 'E': 8, 'F': 18, 'G': 30}

# Create a list of numbers less than 20 and greater than 5
filtered_list = [value for value in numbers_dict.values() if 5 < value < 20]

print("Filtered List:")
print(filtered_list)

count = len(filtered_list)

print(count)