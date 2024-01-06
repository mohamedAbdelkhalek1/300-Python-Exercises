"""
complex_assignment_95:

Write A Desktop Application To Get 5 Color Name From The User In List, Remove Last And First Color And 
    Then Display All The Colors To User.
And Also Display Those Color Which Have 3 Characters.

"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_colors():
    lst = [entry1.get(), entry2.get(), entry3.get(), entry4.get(),entry5.get()]
    lst.pop(0)
    lst.pop(-1)
    Label(root, text= "All The Colors Except Last and First Color :").pack()
    for i in lst:
            Label(root, text= i).pack()
    Label(root, text= "Colors Which Have 3 Characters :").pack()
    for i in lst:
            if len(i)==3:
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
