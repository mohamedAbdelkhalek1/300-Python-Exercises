"""
intermediate_assignment_82:

Create a Desktop Python Program to insert a Button in Window. A message box should be display when user click on the button.

"""


from tkinter import * 
root = Tk()
root.title("Quit Window....")
root.geometry("300x300")

def myfunc():
    msg = Label(root, text="Welcom")
    msg.pack()

btn = Button(root, text="Close this window", command=myfunc)
btn.pack()
root.mainloop()