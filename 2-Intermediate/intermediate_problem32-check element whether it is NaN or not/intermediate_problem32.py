
"""
intermediate_problem32:

Write a Python Numpy program to check element whether it is NaN or not.

"""



import numpy as np
ar = np.array([1,2,3,4,5,6,np.nan, np.inf])
print(ar)


"""
In Python, numpy.nan is a special value used in the NumPy package to represent missing or undefined numerical values.
"nan" stands for Not a Number. The numpy.nan value is considered a special type of floating-point number (float) in Python.

The numpy.nan value is typically used in mathematical operations when the data is missing, invalid,
    or does not have a valid numerical value.
    
For example, if you perform a mathematical operation that involves the numpy.

nan value, the result will also be numpy.nan. This allows you to handle missing data in a convenient and flexible manner.

"""

# Here are some examples of using numpy.nan in NumPy:
# python Copy
import numpy as np

# Create an array with a nan value
arr = np.array([1, 2, np.nan, 4, 5])

# Check if the value is nan
print(np.isnan(arr))  # [False False  True False False]

# Calculate the mean while ignoring nan values
print(np.nanmean(arr))  # 3.0

# Calculate the sum while ignoring nan values
print(np.nansum(arr))  # 12.0

"""

In the above examples, the np.isnan() function is used to check if the value equals numpy.nan or not.
The np.nanmean() and np.nansum() functions are used to calculate the mean and sum, respectively, while ignoring numpy.nan values.

It's important to note that when using numpy.nan in mathematical operations, the result will always be numpy.
nan unless the values are handled separately. Therefore, you may need to check for the presence of numpy.
nan values and handle them appropriately in your applications.
"""