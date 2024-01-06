"""
intermediate_assignment_80:

Create a Desktop Python program to create a window and Insert a Button.

"""
from tkinter import *

window = Tk()
window.title("window")
window.geometry("400x400")

button = Button(window, text="Insert", bg="yellow")
button.pack()

window.mainloop()