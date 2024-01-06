"""
assignment 68:

Write A Python Program That Accepts Six Identity Numbers Of Students,
Clear The List Item And Make Use Of Empty Method To Check, It Has Been Empty Or Not

"""

std_id = []

def check_empty_list(lst):
    # Clear the list items
    # Check if the list is empty or not
    if lst:
        print("The list is not empty.")
    else:
        print("The list is empty.")


for i in range(6): # 0 1 2 3 4 5 
    std_id.append(int(input("Enter std id")))
# print(std_id)

std_id.clear()
print("List is cleared")
print(check_empty_list(std_id))