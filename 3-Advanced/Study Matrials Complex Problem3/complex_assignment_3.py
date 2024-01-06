"""
complex_assignment_3:

Write A Python Program To Get 10 Student Name Store Into List. Display Student Name Randomly.
Don’t Include That Student Name Which User Say.

"""
import random

std = []

for i in range(4):
    std.append(input(f"Enter student number {i+1} : "))
    
random_std = random.choice(std)

print("Random choise student is "+random_std)




# # another solution:
# import random

# std = []

# for i in range(4):
#     std.append(input(f"Enter student number {i+1} : "))
    
# random_std = random.randrange(len(std))

# print("Random choise student is "+std[random_std])


