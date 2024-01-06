"""
complex_problem93

Write A Desktop Application In Python To Generate 10 Number In Order To Display Their Square.

"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_square():
    for i in range(1,11):
        square = str(i)+" having square of "+str(i*i)
        Label(root, text= square).pack()

btn = Button(root, text="Enter", command=get_square)
btn.pack()
root.mainloop()
