"""
complex_problem89:

Write a Desktop application in Python to create a Progress bar widget. 

"""

from tkinter import *
from tkinter.ttk import Progressbar

root = Tk()
root.geometry("400x300")
progress = Progressbar(root, orient=HORIZONTAL, mode="determinate", length="300")
progress.pack()

def progressfunc():
    progress['value']+= 10

btn = Button(root, text="Enter", command=progressfunc)
btn.pack()
root.mainloop()
