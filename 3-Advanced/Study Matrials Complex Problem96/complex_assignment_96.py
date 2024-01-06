"""
complex_assignment_96:

Write A Web Application In Python To Get A String From User To Convert Into Uppercase,
    If Already String In Uppercase Then Display A Message, “String Is Already In Uppercase”  


"""

from tkinter import *
root = Tk()
root.geometry("400x300")

def get_user_str():
    user_s = entry.get()
    
    if user_s.isupper():
        Label(root, text="ALready in uppercase").pack()
    else:
        upper_user_s = user_s.upper()
        Label(root, text="String is converted to uppercase "+str(upper_user_s)).pack()



entry = Entry(root, width=40)
entry.pack(pady=4)

btn = Button(root, text="Enter", command=get_user_str)
btn.pack()
root.mainloop()
