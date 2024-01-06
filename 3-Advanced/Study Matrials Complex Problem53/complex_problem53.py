"""
complex_problem53:

Write a Python Program to extract the html from the page.

"""

import requests
site  = "https://www.jafricode.com"
page = requests.get(url=site)
page_html = page.text()
print(page_html)