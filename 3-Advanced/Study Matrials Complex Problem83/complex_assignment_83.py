"""
complex_assignment_83:

Write a Desktop Application in Python to get a number to check whether it is negative, positive or zero.

"""
from tkinter import *

root = Tk()
root.geometry("600x350")

def check_value():
    num = int(entry.get())
    if num > 0:
        label = Label(root, text="Positive Number").pack()
    elif num < 0:
        label = Label(root, text="Negative Number").pack()
    else:
        label = Label(root, text="Number is equal to Zero").pack()




entry = Entry(root, width="40")
entry.pack(pady=10)

btn = Button(root, text="Enter", command=check_value)
btn.pack()
root.mainloop()