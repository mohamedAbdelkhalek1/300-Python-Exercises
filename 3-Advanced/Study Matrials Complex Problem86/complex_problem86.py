"""
complex_problem86:

Create a Desktop Application in a Python that displays a dialog box asking the user to enter an integer and 
    display its square in console.

"""

from tkinter import *
from tkinter import simpledialog

root = Tk()

number = simpledialog.askinteger("Input","Enter a number", parent=root)
print("Square of your entered number is "+str(number*number))
root.mainloop()
