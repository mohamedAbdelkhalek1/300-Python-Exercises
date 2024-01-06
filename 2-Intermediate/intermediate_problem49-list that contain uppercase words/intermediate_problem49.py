
"""
intermediate_problem49:

Write a Python Program to Create a list from existed list that contain uppercase words

"""

lst = ["jafri","FAISAL","Zamir","ALI","JOHN","Green","PINK"]

new_list = [word for word in lst if word.isupper()]

print(new_list)