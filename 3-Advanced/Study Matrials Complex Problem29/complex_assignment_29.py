"""
complex_assignment_29:

Write a Python program to load csv file using other than pandas library and print the shape of the csv file and display data in the form of string.  

"""
import csv

def load_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
    return data

def print_csv_shape(data):
    num_rows = len(data)
    if num_rows > 0:
        num_columns = len(data[0])
        print("Shape of the CSV file: {} rows, {} columns".format(num_rows, num_columns))
    else:
        print("Empty CSV file.")

def display_csv_data(data):
    for row in data:
        # Convert each row to a string and display
        row_str = ', '.join(row)
        print(row_str)

# Path to the CSV file
csv_file_path = 'E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem29/myfile.csv'

# Load the CSV file
csv_data = load_csv_file(csv_file_path)

# Print the shape of the CSV file
print_csv_shape(csv_data)

# Display the CSV data as a string
display_csv_data(csv_data)