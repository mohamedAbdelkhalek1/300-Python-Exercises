"""
problem 98:

Write A Python Program To Count Prime Number From 1 To 100

"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num %i == 0:
            return False
    return True

count = 0
for i in range(100):
    if is_prime(i):
        count += 1
        
print(f"Prime Number From 1 To 100 = {count} Numbers")