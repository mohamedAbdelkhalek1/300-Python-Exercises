"""
intermediate_assignment_93:

Write a Python Program to display odd number from array using OOP.

"""
from array import *

class ArrayProcess:
    def __init__(self, arr):
        self.arr = arr
        print("array : ", self.arr)
        
    def get_odd_numbers(self):
        for i in self.arr:
            if i%2 != 0:
                print(i)



ar = array('i',[1,1,1,13,4,5,6,7])

ArrayProcess(ar).get_odd_numbers()