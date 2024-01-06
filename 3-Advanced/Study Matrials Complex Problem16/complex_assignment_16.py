"""
complex_assignment_16:

Write A Python Program To Create A CSV File To Store Odd Number As Generated From 200 To 100.

"""
import csv

# Generate odd numbers from 200 to 100
odd_numbers = [num for num in range(200, 99, -1) if num % 2 != 0]

# Define the CSV file path
csv_file = 'E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem16/odd_numbers.csv'

# Write the odd numbers to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Odd Numbers'])
    writer.writerows([[num] for num in odd_numbers])

print(f'Odd numbers have been saved to {csv_file}.')