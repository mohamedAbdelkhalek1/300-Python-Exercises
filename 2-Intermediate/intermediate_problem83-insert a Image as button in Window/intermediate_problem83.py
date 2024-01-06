"""
intermediate_problem83:

Create a Desktop Python Program to insert a Image as button in Window.

"""

from tkinter import * 
root = Tk()
root.title("Inserting Image....")
root.geometry("300x300")

img = PhotoImage(file="E:/bulding/python_exercises/2-Intermediate/intermediate_problem83-/R.png")
btn = Button(root, image=img)
btn.pack(padx=10, pady=10)
root.mainloop()

