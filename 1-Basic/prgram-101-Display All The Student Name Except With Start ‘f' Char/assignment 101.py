"""
assignment 101:

Write A Python Program To Display All The Student Name Except Start With ‘f‘ And End With ‘n’ Char

"""

std_list = ['ali','kami','faisal','fazen','yaseen']
print(std_list)
for i in std_list:
    if not (i.startswith('f') or  i.endswith("n")):
        print(i)