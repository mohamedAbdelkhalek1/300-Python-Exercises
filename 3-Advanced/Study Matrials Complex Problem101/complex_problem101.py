"""
complex_problem101:

Write A Desktop Application To Get A String From User To Save In Text File.

"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_string():
    user_str = entry.get()
    file = open("E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem101/save_user_str.txt","w+")
    file.write(user_str)
    file.close()
    Label(root, text=user_str).pack()
entry = Entry(root, width=40)
entry.pack(pady=4)

btn = Button(root, text="Enter", command=get_string)
btn.pack()
root.mainloop()
