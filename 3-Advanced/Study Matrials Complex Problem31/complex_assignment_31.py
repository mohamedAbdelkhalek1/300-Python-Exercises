"""
complex_assignment_31:

Write a Pandas program to create a subset of a given series. Add some modifications.

"""
import pandas as pd

s = pd.Series([1,2,3,4,5,6,61])
print(s)

#subset of even number 
new_ps = s[s%2==0]

#subset of first 5 items 
new_ps2 = s.head(5)

print(new_ps)
print(new_ps2)