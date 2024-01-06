
"""
problem 34:

Write A Python Program To Get 5 Color name From The User In List, Display That List, Remove Last Color And Then Display All The Colors to User

"""


# get 5 color from the user
# display color
# rm last color
# display

color_lst = []
for i in range(5): # 0 1 2 3 4
    color_lst.append(input(f"Enter a name of color {i+1} : "))
    
print("List color element "+str(color_lst))
color_lst.pop()
print("List color element "+str(color_lst))

