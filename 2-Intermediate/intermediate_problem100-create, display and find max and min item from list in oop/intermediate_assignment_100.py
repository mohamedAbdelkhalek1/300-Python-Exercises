"""
intermediate_assignment_100:

Write a Python Program to create a list on run time, display list element,
and also find max and min item from list of integers using Procedural Programming.

"""
def matrix():
    # Create the list
    lst = []
    for i in range(5):
        item = int(input(f"Enter number {i+1} : "))
        lst.append(item)
    
    # Print  the list    
    print(lst)
    
    # Get max & min
    print("Max = "+str(max(lst)))
    print("Min = "+str(min(lst)))
    
matrix()




# #another solution : 
# def create_list():
#     numbers = []
#     n = int(input("Enter the number of elements in the list: "))
#     for i in range(n):
#         num = int(input("Enter element {}: ".format(i + 1)))
#         numbers.append(num)
#     return numbers

# def display_list(numbers):
#     print("List elements:")
#     for num in numbers:
#         print(num)

# def find_max(numbers):
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num

# def find_min(numbers):
#     min_num = numbers[0]
#     for num in numbers:
#         if num < min_num:
#             min_num = num
#     return min_num

# # Main program
# my_list = create_list()
# display_list(my_list)

# max_number = find_max(my_list)
# min_number = find_min(my_list)

# print("Maximum number in the list:", max_number)
# print("Minimum number in the list:", min_number)