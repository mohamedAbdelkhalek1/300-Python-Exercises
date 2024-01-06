"""
intermediate_assignment_76:

Write a Python program to get the size, permissions, owner, and device of a specified path.

"""

import os

def get_path_info(path):
    stat_info = os.stat(path)

    # Get size of the path in bytes
    size = stat_info.st_size

    # Get permissions of the path
    permissions = oct(stat_info.st_mode)[-3:]

    # Get owner of the path
    owner = stat_info.st_uid

    # Get device of the path
    device = stat_info.st_dev

    return size, permissions, owner, device

# Example usage
path = 'E:/bulding/python_exercises/2-Intermediate/intermediate_problem76-/intermediate_problem76.py'
size, permissions, owner, device = get_path_info(path)

# Print the path information
print("Size:", size, "bytes")
print("Permissions:", permissions)
print("Owner:", owner)
print("Device:", device)