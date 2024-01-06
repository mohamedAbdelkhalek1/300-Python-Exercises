"""
complex_assignment_82:

Create a Desktop Application in Python to count total number of words in a string, spaces, characters (without spaces) to user.

"""

from tkinter import *

root = Tk()
root.geometry("600x250")

def get_value():
    user_st = entry.get()
    sp = 0
    for i in user_st:
        if i.isspace():
            sp += 1
    total_words = sp + 1
    total_char_without_spaces = len(user_st) - sp
    Label(root, text="Total Words = "+str(total_words)).pack()
    Label(root, text="Total Spaces = "+str(sp)).pack()
    Label(root, text="Total Char without spaces = "+str(total_char_without_spaces)).pack()



entry = Entry(root, width="40")
entry.pack(pady=10)

btn = Button(root, text="Enter", command=get_value)
btn.pack()
root.mainloop()