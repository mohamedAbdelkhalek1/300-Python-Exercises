"""
intermediate_problem80:

Create a Desktop Python program to create a window and set geometry that should be fixed. And Disable resize functionality

"""


from tkinter import * 
root = Tk()
root.title("Window Title Example...")
root.geometry("500x500")
root.resizable(False, False)
root.mainloop()