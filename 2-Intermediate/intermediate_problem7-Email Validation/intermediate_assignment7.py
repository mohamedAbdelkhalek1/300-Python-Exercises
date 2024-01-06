"""
intermediate_assignment7:

Write A Python Program To Get A URL from user to check whether it is valid URL or not.

"""

import re

url = input("Enter a Web Title ")
pattern = r"(https?://)(www.)?(\w+)\.(\w+):?(\d+)?/?(.+)"

match  = re.search(pattern, url)

if match :
    print("URL is valid")
else:
    print("URL is invalid")