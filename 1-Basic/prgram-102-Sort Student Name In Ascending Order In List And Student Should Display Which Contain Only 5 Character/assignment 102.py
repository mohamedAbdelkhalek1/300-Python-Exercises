"""
assignment 102:

Write A Python Program To Sort Student Name In Descending Order In List And Put A ‘.’ At The End Of Every Student Name

"""

# std_list = ['aliee','kami','faisa','faiz','yash']
# std_list.sort(reverse=True)
# print(std_list)
# for i in range(len(std_list)):
#     std_list[i] = std_list[i].ljust(len(std_list[i])+1,".")
    
# print(std_list)


# another solution with short for
student_names = ["John", "Alice", "Franklin", "Steven", "Megan", "Fiona", "Kevin", "Jason"]

# Sort the student names in descending order
student_names.sort(reverse=True)

# Add '.' at the end of each student name
student_names = [name + '.' for name in student_names]

# Print the sorted names
for name in student_names:
    print(name)