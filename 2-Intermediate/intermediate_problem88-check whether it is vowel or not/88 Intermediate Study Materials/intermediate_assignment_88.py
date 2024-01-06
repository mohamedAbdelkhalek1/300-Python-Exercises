"""
intermediate_assignment_88:

Write a Desktop Python program to get a string from user to reverse.

"""

from tkinter import * 
win = Tk()
win.title("Get reverse")
win.geometry("500x500")

def get_value():
    txt = e1.get()
    Label(win, text=txt[-1::-1]).pack()
  
Label(win, text="Enter the text").pack()
e1 = Entry(win, width=30)
e1.pack()


Button(win, text="Reverse", command=get_value).pack()
win.mainloop()
