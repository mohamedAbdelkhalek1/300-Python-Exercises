"""
assignment 83:

Write A Python Program To Get Name From A List, That End at ‘f'

"""

person_name = ['Ali','Yousef','faisal','faiz','ahmad','fatir','ray']

for i in person_name:
    if(i.endswith('f')):
        print(i)
        



# # Another solution    
# for i in person_name:
#     if(i[-1] == 'f'):
#         print(i)