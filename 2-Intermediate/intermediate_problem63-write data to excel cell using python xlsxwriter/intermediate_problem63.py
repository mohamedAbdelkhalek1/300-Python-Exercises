"""
intermediate_problem63:

Write a Python Program to write data to excel cell using python xlsxwriter.

"""

import xlsxwriter

wb = xlsxwriter.Workbook("xlswriter_wb2.xlsx")

wb_sheet = wb.add_worksheet()

wb_sheet.write('A1',"Faisal Zamir")
wb_sheet.write('B1',"Python")
wb_sheet.write('E4',"js")

wb.close()