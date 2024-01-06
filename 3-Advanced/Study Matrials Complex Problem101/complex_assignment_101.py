"""
complex_assignment_101:

Write A Desktop Application To Get A String From User. Display Required String Sub Part Using Slicing Method.

"""
from tkinter import *
root = Tk()
root.geometry("400x300")

def get_string():
    user_str = entry.get()
    Label(root, text=user_str[3:6]).pack()
entry = Entry(root, width=40)
entry.pack(pady=4)

btn = Button(root, text="Enter", command=get_string)
btn.pack()
root.mainloop()
