"""
intermediate_problem84:

Write a Desktop Python program to create a Checkboxes.

"""

from tkinter import * 
root = Tk()
root.title("Create Checkboxes....")
root.geometry("300x300")
c1 = Checkbutton(text="I am student")
c1.pack()

c2 = Checkbutton(text="I am Teacher")
c2.pack()

c3 = Checkbutton(text="I am Pakistani")
c3.pack()
root.mainloop()