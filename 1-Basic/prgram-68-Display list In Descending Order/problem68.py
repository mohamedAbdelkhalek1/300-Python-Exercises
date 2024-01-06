
"""
problem 68:

Write A Python Program That Accepts Six Identity Numbers Of Students As Input And Display In Descending Order. 

"""

# To get id of std
# display in dcs

std_id = []

for i in range(6): # 0 1 2 3 4 5 
    std_id.append(int(input("Enter std id")))
std_id.sort(reverse = True)
print(std_id)