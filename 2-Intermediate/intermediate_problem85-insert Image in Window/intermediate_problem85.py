"""
intermediate_problem85:

Create a Desktop Python Program to insert Image in Window.

"""

from tkinter import * 
win = Tk()
win.title("Image as backgorund.,,")
# win.geometry("300x300")
img = PhotoImage(file="E:/bulding/python_exercises/2-Intermediate/intermediate_problem85-/R.png")
l = Label(win, image=img)
l.pack()
win.mainloop()

