"""
intermediate_assignment_91:

Write a Python Program To find array size in bytes using OOP.

"""
from array import *

class ArrProcess:
    def __init__(self):
        print("Welcom to array processe")
        
    @classmethod
    def get_arr_size(cls, arr):
        cls.arr = arr
        one_item_size = cls.arr.itemsize
        total_len = len(cls.arr)
        total_size = total_len * one_item_size
        print(str(total_size)+ " Byte")


ar = array('i',[1,2,3,13,4,5,6,7])
ArrProcess.get_arr_size(ar)