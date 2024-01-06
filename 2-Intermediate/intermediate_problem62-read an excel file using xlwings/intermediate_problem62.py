"""
intermediate_problem62:

Write a Python program to read an excel file using xlwings 

"""

import xlwings

wb = xlwings.Book("xlwings.xlsx").sheets["Sheet1"]
data = wb.range("A1:E1").value
print(data)