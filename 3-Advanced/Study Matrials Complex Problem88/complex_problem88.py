"""
complex_problem88:

Write a Desktop Application in Python to create a Listbox widget.

"""

from tkinter import *



root = Tk()

lst = Listbox(root, bd=10, fg="yellow", bg="black", cursor="arrow")
lst.insert(0,"Python")
lst.insert(1,"C++")
lst.insert(2,"HTML")

lst.pack()
"""
cursors:

"arrow"
"circle"
"clock"
"cross"
"dotbox"
"exchange"
"fleur"
"heart"
"heart"
"man"
"mouse"
"pirate"
"plus"
"""
root.mainloop()
