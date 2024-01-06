"""
assignment 98:

Write A Python Program To Get Prime Number From 100 To 1

"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num %i == 0:
            return False
    return True

count = 0
for i in range(100,0,-1):
    if is_prime(i):
        count += 1
        
print(f"Prime Number From 100 To 1 = {count} Numbers")