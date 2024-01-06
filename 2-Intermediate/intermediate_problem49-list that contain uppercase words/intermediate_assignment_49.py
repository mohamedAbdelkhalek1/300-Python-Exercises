"""
intermediate_assignment_49:

Write a Python Program to Create a list from existed list that contain lowercase words

"""

lst = ["jafri","FAISAL","Zamir","ALI","JOHN","Green","PINK"]

new_list = [word for word in lst if word.islower()]

print(new_list)