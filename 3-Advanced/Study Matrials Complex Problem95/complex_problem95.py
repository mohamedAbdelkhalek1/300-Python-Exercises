"""
complex_problem95:

Write A Desktop Application To Get 5 Color name From The User In List,
   And Then Display All The Colors to User Except Last and First Color

"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_colors():
    lst = [entry1.get(), entry2.get(), entry3.get(), entry4.get(),entry5.get()]
    for i in lst[1:4]:
            Label(root, text= i).pack()

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
