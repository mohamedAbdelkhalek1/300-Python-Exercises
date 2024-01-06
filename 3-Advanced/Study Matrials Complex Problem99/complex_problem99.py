"""
complex_problem99:

Write A Desktop Application In Python To Get 5 Number From User To Store In List.
Find Addition And Product Of All That Number And Display Result To User.

"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_number():

    lst = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()),int(entry5.get())]

    addition = 0 
    product = 1
    for i in lst:
        addition += i
        product *= i
    Label(root, text="Addition = "+str(addition)).pack()
    Label(root, text="Product = "+str(product)).pack()



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
