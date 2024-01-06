"""
intermediate_assignment_87:

Write a Desktop Python program to get a string from user to change uppercase if user string is in lowercase.

"""

from tkinter import * 
win = Tk()
win.title("Get UPPERCASE")
win.geometry("500x500")

def get_value():
    txt = e1.get()
    Label(win, text=txt.upper()).pack()
  
Label(win, text="Enter the text").pack()
e1 = Entry(win, width=30)
e1.pack()


Button(win, text="UPPER", command=get_value).pack()
win.mainloop()
