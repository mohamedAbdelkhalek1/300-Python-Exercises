"""
intermediate_assignment_21:

Write a Python program to get 5 number from user to store in a list.  Add all that number to each other using list comprehension.


"""

numbers = [5,7,8,4,6,1]

total = sum([num for num in numbers])     #list comprehension
#total = sum(nubers)

# Print the result
print("The sum of the numbers is:", total)