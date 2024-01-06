"""
complex_assignment_89:

Write a Desktop application in Python to create a scroll bar. 

"""
from tkinter import *
from tkinter.ttk import Scrollbar

root = Tk()
root.geometry("400x300")

scroll = Scrollbar(root)
scroll.pack(side=RIGHT)


root.mainloop()
