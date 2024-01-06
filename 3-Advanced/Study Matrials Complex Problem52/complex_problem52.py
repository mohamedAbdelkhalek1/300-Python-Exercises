"""
complex_problem52:

Write a Python Program to Open the url using urllib library

"""

import urllib.request

site = urllib.request.urlopen("https://www.jafricode.com")
code = site.getcode()
print(code)