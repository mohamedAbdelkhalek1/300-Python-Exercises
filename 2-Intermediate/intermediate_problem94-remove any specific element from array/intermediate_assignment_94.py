"""
intermediate_assignment_94:

Write a Python Program to remove any specific element from array using OOP. 

"""
# Remove with index
from array import *
class ArrayProcess:
    def __init__(self, arr):
        self.arr = arr
        print("array : ", self.arr)
        
    def remove_item(self):
        n = int(input("Enter position of element which you want to remove"))
        ar.pop(n-1) #2, 3-1 = 2
        print(ar)


ar = array('i',[1,1,1,13,4,5,6,7])
ArrayProcess(ar).remove_item()




# # Remove with value
# from array import *
# class ArrayProcess:
#     def __init__(self, arr):
#         self.arr = arr
#         print("array : ", self.arr)
        
#     def remove_item(self):
#         n = int(input("Enter the element which you want to remove"))
#         ar.remove(n)
#         print(ar)


# ar = array('i',[1,1,1,13,4,5,6,7])
# ArrayProcess(ar).remove_item()