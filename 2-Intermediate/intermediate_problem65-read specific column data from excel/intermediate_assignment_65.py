"""
intermediate_assignment_65:

Write a Python Program to use append method in excel using python

"""
import pandas as pd

# Load the existing Excel file
file_path = 'E:/bulding/python_exercises/2-Intermediate/intermediate_problem65-/xlwings.xlsx'
df_existing = pd.read_excel(file_path)

# Create a new DataFrame with the data you want to append
new_data = {'Column1': ['Value1', 'Value2', 'Value3'],
            'Column2': [1, 2, 3]}
df_new = pd.DataFrame(new_data)

# Append the new data to the existing DataFrame
df_appended = df_existing._append(df_new, ignore_index=True)

# Write the appended DataFrame back to the Excel file
df_appended.to_excel(file_path, index=False)

print('Data appended successfully.')