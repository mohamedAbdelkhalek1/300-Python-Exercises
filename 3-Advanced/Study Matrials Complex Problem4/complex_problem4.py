"""
complex_problem4:

Write a Pandas program to convert a Panda module Series to Python list. 

"""


import pandas 
ps = pandas.Series([11,223,43,54,5])
print(ps)
print(type(ps))
ps_list = ps.tolist()
print(ps_list)
print(type(ps_list))
print(ps_list)