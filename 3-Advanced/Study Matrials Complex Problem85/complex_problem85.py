"""
complex_problem85:

Create a Desktop Application to display different types of message box.

"""

from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.showerror("Error title","This is the error in your system")
messagebox.showinfo("information title","We are provding something to you")
messagebox.showwarning("Warning title","Dont use again this one")

root.mainloop()
