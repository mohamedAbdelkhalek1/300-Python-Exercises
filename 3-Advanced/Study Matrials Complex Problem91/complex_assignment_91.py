"""
complex_assignment_91:

Write A Desktop Application In Python To Get 5 Number From User To Store In A List. And Display List Items in Ascending order

"""
from tkinter import *

root = Tk()
root.geometry("400x300")

def result():
    lst =  [int(num1.get()), int(num2.get()),int(num3.get()), int(num4.get()), int(num5.get()) ]
    sorted_lst = sorted(lst)
    Label(root, text="List Items in Ascending order" + str(sorted_lst)).pack()



num1 = Entry(root, width=40)
num1.pack()
num2 = Entry(root, width=40)
num2.pack()
num3 = Entry(root, width=40)
num3.pack()
num4 = Entry(root, width=40)
num4.pack()
num5 = Entry(root, width=40)
num5.pack()
btn = Button(root, text="Enter", command=result)
btn.pack()
root.mainloop()
