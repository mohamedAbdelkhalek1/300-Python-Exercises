"""
assignment 60:

Write A Python Program To Get 5 Author Name With Their Book Name And Display First Author With It's Book Name

"""


# to get 5 author with book
# display first author and book

author_books = {}

for i in range(5):
    author_name = input("Enter author name") 
    book_name = input("Enter its book name")
    author_books[author_name] = book_name

print("first auther is "+str(list(author_books.keys())[0]))
print("first book is "+str(list(author_books.values())[0]))
#print(author_books)

