"""
intermediate_problem54:

Write a Numpy program to perform addition, subtraction, division and multiplication on Array Element.    

"""


import numpy as np
ar1 = np.array([1,2,3,4])
ar2 = np.array([3,4,5,6])
print(ar1)
print(ar2)
addition = np.add(ar1, ar2)
# addition = ar1 + ar2
print("Addition = " +str(addition))

sub = np.subtract(ar1, ar2)
# sub = ar1 - ar2
print("Subtract = " +str(sub))

multiply = np.multiply(ar1, ar2)
# multiply = ar1 * ar2
print("multiply = " +str(multiply))

divide = np.divide(ar1, ar2)
# divide = ar1 / ar2
print("divide = " +str(divide))