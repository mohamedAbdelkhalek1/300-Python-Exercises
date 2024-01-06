"""
complex_assignment_53:

Write a Python Program to extract the html from the page. Using other than requests method.

"""

import urllib.request

url = "https://www.jafricode.com"

try:
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)
except urllib.error.URLError as e:
    print("Error: ", e.reason)
