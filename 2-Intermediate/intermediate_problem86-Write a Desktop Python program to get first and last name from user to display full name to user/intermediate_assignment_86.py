"""
intermediate_assignment_86:

Write a Desktop Python program to get a number from user to display its cube.

"""
from tkinter import * 

win = Tk()
win.title("Cube of number")
win.geometry("500x500")

def get_value():
    num = int(e1.get())
    Label(win, text=num**3).pack()

l1 = Label(win, text="Enter the number").pack()
e1 = Entry(win, width=30)
e1.pack()


Button(win, text="Cube", command=get_value).pack()
win.mainloop()
