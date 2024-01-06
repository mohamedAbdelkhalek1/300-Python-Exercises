"""
complex_assignment_7:

Write A Desktop Application In Python To Get 5 Number From User To Store In A List. Display Only Odd Number From List.

"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_number():
    lst = [entry1.get(), entry2.get(), entry3.get(), entry4.get(),entry5.get()]
    for i in lst:
        if i%2 != 0:
            print(i)
            Label(root, text=i).pack()

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
btn = Button(root, text="Enter", command=get_number)
btn.pack()
root.mainloop()
