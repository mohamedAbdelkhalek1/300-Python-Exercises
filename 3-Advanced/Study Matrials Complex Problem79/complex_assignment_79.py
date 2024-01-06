
"""
complex_assignment_79:

Write Desktop application in A Python Program To Get 3 Author Name With Their Book Name And Display Last Author With It's Book Name

"""

from tkinter import *

def get_Force():
    author3_data = {str(author3_name_entry.get()) : str(author3_book_entry.get())}
    author3_label = Label(window, text = "author3 = "+str(author3_data))
    author3_label.pack()


window = Tk()
window.geometry("500x500")
window.title("Add half")

author1_name_label = Label(window, text = 'Author 1 Name', font=('calibre',10, 'bold')).pack()
author1_name_entry = Entry(window, width=50, font=('calibre',10,'normal'))
author1_name_entry.pack()
autho1_book_label = Label(window, text = 'Author 1 book', font=('calibre',10, 'bold')).pack()
author1_book_entry = Entry(window, width=50, font=('calibre',10,'normal'))
author1_book_entry.pack()

author2_name_label = Label(window, text = 'Author 2 Name', font=('calibre',10, 'bold')).pack()
author2_name_entry = Entry(window, width=50, font=('calibre',10,'normal'))
author2_name_entry.pack()
author2_book_label = Label(window, text = 'Author 2 book', font=('calibre',10, 'bold')).pack()
author2_book_entry = Entry(window, width=50, font=('calibre',10,'normal'))
author2_book_entry.pack()

author3_name_label = Label(window, text = 'Author 3 Name', font=('calibre',10, 'bold')).pack()
author3_name_entry = Entry(window, width=50, font=('calibre',10,'normal'))
author3_name_entry.pack()
author3_book_label = Label(window, text = 'Author 3 book', font=('calibre',10, 'bold')).pack()
author3_book_entry = Entry(window, width=50, font=('calibre',10,'normal'))
author3_book_entry.pack()



btn = Button(window, text="Result", command= get_Force).pack()


window.mainloop()