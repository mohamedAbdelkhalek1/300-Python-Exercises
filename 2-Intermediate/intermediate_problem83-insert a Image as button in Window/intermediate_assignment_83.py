"""
intermediate_assignment_83:

Create a Desktop Python Program to insert a Image as button with text in Window.

"""

from tkinter import * 
root = Tk()
root.title("Inserting Image....")
root.geometry("300x300")

img = PhotoImage(file="E:/bulding/python_exercises/2-Intermediate/intermediate_problem83-/R.png")
btn = Button(root, image=img, text="Click Me")
btn.pack()
txt = Label(root, text="Download")
txt.pack()
root.mainloop()
