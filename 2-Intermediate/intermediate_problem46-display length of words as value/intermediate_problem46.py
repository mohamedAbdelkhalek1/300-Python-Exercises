"""
intermediate_problem46:

Write a Python Program Create dictionary from existed dictionary which display length of words as value

"""


d = {"name":"Faisal Zamir","age":13,"course":"Python","City":"Dera Ismail Khan"}
print(d)
new_dic = {k:len(k)  for k in d.keys()}

print(new_dic)