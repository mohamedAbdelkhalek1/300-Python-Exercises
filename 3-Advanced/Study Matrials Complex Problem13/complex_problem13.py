"""
complex_problem13:


"""

import pandas as pd
lst = []

for i in range(5):
    lst.append(int(input("Enter a number")))

print("List Items "+str(lst))
ps = pd.Series(lst)
print("Pandas Items "+str(ps))
ps_ = pd.Series(lst, index=['a','b','c','d','e'])
print(ps_)

