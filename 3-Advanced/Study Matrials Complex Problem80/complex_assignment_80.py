
"""
complex_assignment_80:

Write Desktop application in A Python Program To Get 3 Author Name With Their Book Name And Display Last Author With It's Book Name

"""

from tkinter import *

def get_upper():
    word_list = [ str(word1_entry.get()), str(word2_entry.get()), str(word3_entry.get()) ]
    upper_word_list = [i for i in word_list if i.isupper()]
    upper_word_list_label = Label(window, text = "upper_word_list = "+str(upper_word_list))
    upper_word_list_label.pack()


window = Tk()
window.geometry("500x500")
window.title("Add half")

word1_label = Label(window, text = 'write a word 1', font=('calibre',10, 'bold')).pack()
word1_entry = Entry(window, width=50, font=('calibre',10,'normal'))
word1_entry.pack()


word2_label = Label(window, text = 'write a word 2', font=('calibre',10, 'bold')).pack()
word2_entry = Entry(window, width=50, font=('calibre',10,'normal'))
word2_entry.pack()


word3_label = Label(window, text = 'write a word 3', font=('calibre',10, 'bold')).pack()
word3_entry = Entry(window, width=50, font=('calibre',10,'normal'))
word3_entry.pack()

btn = Button(window, text="Result", command= get_upper).pack()


window.mainloop()