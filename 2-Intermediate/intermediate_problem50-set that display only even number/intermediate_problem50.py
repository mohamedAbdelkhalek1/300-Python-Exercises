"""
intermediate_problem50:

Write a Python Program to Create set that display only even number

"""


st = set()

for i in range(5):
    st.add(int(input("Enter a set item")))
# print(st)

for i in st:
    if i%2 == 0:
        print(i)