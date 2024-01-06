"""
intermediate_assignment_92:

Write a Python Program to count any array element from existed array using OOP

"""

from array import *

class ArrayProcess:
    def __init__(self, arr):
        self.arr = arr
        print(self.arr)
        
    def get_item_count(self):
        item = int(input("Enter a number"))
        result = self.arr.count(item)
        print(str(result)+ " time "+str(item)+" existed")


ar = array('i',[1,1,1,13,4,5,6,7])

ArrayProcess(ar).get_item_count()