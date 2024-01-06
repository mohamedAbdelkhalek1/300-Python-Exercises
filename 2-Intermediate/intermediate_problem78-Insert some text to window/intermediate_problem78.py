
"""
intermediate_problem78:

Create a Desktop Python program to create a window and Insert some text to window

"""

from tkinter import * 
root = Tk()
root.title("Window Title Example...")
root.geometry("500x500")
text = Label(root, text="How are you")
text.pack(pady= 30)
text1 = Label(root, text="Another text....")
text1.pack()
root.mainloop()