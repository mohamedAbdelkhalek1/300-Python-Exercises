"""
intermediate_assignment_60:

Write a Python Numpy Program to Check whether an array contains a specified row.

"""
import numpy as np

# if row in array form:
def contains_row(arr, row):
    return any(np.array_equal(row, r) for r in arr)

# Example usage
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

row1 = np.array([4, 5, 6])
row2 = np.array([0, 0, 0])

print(contains_row(arr, row1))  # True
print(contains_row(arr, row2))  # False


















# # if row in list form:
# ar = np.array([
#     [2.3, 5.2],
#     [4.1,5.3]
# ])
# print(ar)

# row = [4.1,5.3]

# if row in ar:
#     print("founded")
# else:
#     print("Not found")