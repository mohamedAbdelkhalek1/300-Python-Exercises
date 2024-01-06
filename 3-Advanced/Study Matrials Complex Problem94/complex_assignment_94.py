"""
complex_assignment_94:

Write A Desktop Application In Python To Get 5 Color Name From User And Store In The List And Display Color Name With Reverse order.

"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_colors():
    lst = [entry1.get(), entry2.get(), entry3.get(), entry4.get(),entry5.get()]
    for i in lst:
        list_items = i +" and Color Name With Reverse order:  "+i[-1::-1]+" char"
        Label(root, text=list_items).pack()

entry1 = Entry(root, width=40)
entry1.pack(pady=4)
entry2 = Entry(root, width=40)
entry2.pack(pady=4)
entry3 = Entry(root, width=40)
entry3.pack(pady=4)
entry4 = Entry(root, width=40)
entry4.pack(pady=4)
entry5 = Entry(root, width=40)
entry5.pack(pady=4)
btn = Button(root, text="Enter", command=get_colors)
btn.pack()
root.mainloop()
