"""
assignment 55:

Write A Python Program To Convert date to milliseconds 

"""

from datetime import datetime as dt

start_date = dt.min

date = dt.now()

differ = date - start_date         #in dayes

print(differ.total_seconds()*1000," MS")