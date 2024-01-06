"""
intermediate_assignment_67:

Write a Python Program to copy data from one excel sheet to another

"""
import pandas as pd

def copy_excel_data(source_file, source_sheet, destination_file, destination_sheet):
    # Read the source Excel file
    df_source = pd.read_excel(source_file, sheet_name=source_sheet)

    # Create a new Excel writer object
    writer = pd.ExcelWriter(destination_file, engine='xlsxwriter')

    # Write the data to the destination sheet
    df_source.to_excel(writer, sheet_name=destination_sheet, index=False)

    # Save the changes and close the writer
    writer.save()
    writer.close()

# Example usage
source_file = 'source.xlsx'
source_sheet = 'Sheet1'
destination_file = 'destination.xlsx'
destination_sheet = 'Sheet2'

copy_excel_data(source_file, source_sheet, destination_file, destination_sheet)