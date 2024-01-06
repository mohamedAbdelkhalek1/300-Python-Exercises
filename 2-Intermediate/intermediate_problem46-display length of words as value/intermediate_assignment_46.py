"""
intermediate_assignment_46:

Write a Python Program Create a dictionary that displays the length of words as key. It should display the length of the value.

"""

d = {"name":"Faisal Zamir","age":13,"course":"Python","City":"Dera Ismail Khan"}
print(d)

new_dic = {len(str(v)):v  for v in d.values()}

print(new_dic)