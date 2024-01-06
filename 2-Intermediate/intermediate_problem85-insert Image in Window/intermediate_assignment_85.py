"""
intermediate_assignment_85:

Create a Desktop Python Program to insert Image in Window when a user click on button.

"""

from tkinter import * 
win = Tk()
win.title("Image as backgorund.,,")
# win.geometry("300x300")

def func():
    img = PhotoImage(file="E:/bulding/python_exercises/2-Intermediate/intermediate_problem85-/R.png")
    l = Label(win, image=img)
    l.pack()
    
button = Button(win, text="Click", command=func)
button.pack()

win.mainloop()

