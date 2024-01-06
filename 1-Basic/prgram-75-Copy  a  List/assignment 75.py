"""
assignment 75:

Write A Python Program To Get 10 Number From The User, Store Into List, Find Their Products And Sum.
Then Add Both Result To Display To User

"""
numbers = []
sum = 0
product = 1

for i in range(10):
    numbers.append(int(input(f"Enter number {i+1} : ")))
    sum += numbers[i]
    product *= numbers[i]
    
print("Input numbers : ",numbers)
print("Sum of Numbers = ",sum)
print("Product of Numbers = ",product)
print("Result of adding sum and product = ",product+sum)