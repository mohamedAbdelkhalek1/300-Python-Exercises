"""
complex_assignment_98:

Write A Desktop Application In Python To Get a String From the User To Display Those Characters that Existed At an Odd Index Number.

"""
from tkinter import *
root = Tk()
root.geometry("400x300")

def get_str():
    user_str = entry.get()
    Label(root, text="Characters that Existed At an Odd Index Number: ").pack()
    for i in user_str[1::2]:
        Label(root, text=str(i)).pack()
    

entry = Entry(root, width=40)
entry.pack(pady=4)

btn = Button(root, text="Enter", command=get_str)
btn.pack()
root.mainloop()
