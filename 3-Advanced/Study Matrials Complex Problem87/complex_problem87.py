"""
complex_problem87:

Create a Desktop Application in Python that displays a dialog asking the user to enter his / her name and age 
    and display name with age in window. Hi NAME! Your age is AGE

"""

from tkinter import *
from tkinter import simpledialog

root = Tk()

age = simpledialog.askinteger("Input","Enter your age", parent=root)
name = simpledialog.askstring("Input","Enter your name", parent=root)
label = Label(root, text = f"Hi {name} Your age is {age}").pack()
root.mainloop()
