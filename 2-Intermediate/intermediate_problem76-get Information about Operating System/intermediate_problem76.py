"""
intermediate_problem76:

Write a Python Program to get Information about Operating System.

"""

import os 
import platform

os_Name = os.name
print("Operating System Name = "+str(os_Name))
system = platform.system()
print("System Name = "+str(system))

release = platform.release()
print("System Release = "+str(release))