"""
problem 33:

Write A Python Program To Get Element From The User, Store In The List, And Count That Element And Display Result To User

"""


lst = []

n = int(input("How many elements to store? : "))

for i in range(n):
    lst.append(input(f"Enter input number {i+1}: "))
    
print("List : ",str(lst))
