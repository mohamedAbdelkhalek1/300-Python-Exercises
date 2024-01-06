"""
intermediate_assignment_75:

Write a Python program to take Python data from user to convert into JSON Data.

"""
import json 

py_obj = {"name":"faisal","age":12,"course":"Python"}
print(py_obj)
print(type(py_obj))

print("After converting...")

json_obj = json.dumps(py_obj)
print(json_obj)
print(type(json_obj))