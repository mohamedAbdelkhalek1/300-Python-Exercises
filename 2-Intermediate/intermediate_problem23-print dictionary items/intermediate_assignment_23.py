"""
intermediate_assignment_23:

Write a Python program to create an alpha string-based dictionary to print dictionary items in uppercase. 

"""

d = {1:"Red",2:"Blue",3:"Yellow",4:"Black",5:"Green"}

for k,v in d.items():
    print(str(k).upper() +"\t"+str(v).upper())