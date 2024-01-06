"""
complex_assignment_18:

Write A Python Program To Get RAM and CPU Usage Of Computer

"""


"""
CPU usage or utilization refers to the time taken by a computer to process some information.
RAM usage or MAIN MEMORY UTILIZATION on the other hand refers to the amount of time RAM is used by
    a certain system at a particular time.
Both of these can be retrieved using Python
"""



# import os
# import psutil


# #Get current CPU usage using psutil
# # Calling psutil.cpu_precent() for 4 seconds
# print('The CPU usage is: ', psutil.cpu_percent(4))


# #Get current CPU usage using the OS module
# # The psutil.getloadavg() provides the load information of the CPU in the form of a tuple.
# # The psutil.getloadavg() runs in the background and the results get updated every 5 seconds.
# # The os.cpu_count() returns the number of CPUs in the system.

# # Getting loadover15 minutes
# load1, load5, load15 = psutil.getloadavg()
 
# cpu_usage = (load15/os.cpu_count()) * 100
 
# print("The CPU usage is : ", cpu_usage)

##############################################################################################


#Get current RAM usage in Python

# Importing the library
import psutil
import os

 
# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)



#Get current RAM usage using the OS module
# Getting all memory using os.popen()
total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
 
# Memory usage
print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))