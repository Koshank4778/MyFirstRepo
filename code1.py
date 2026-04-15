books = ["Math", "Science"]

def show_books():
    print("Available books:")
    for book in books:
        print(book)

def borrow_book(book):
    if book in books:
        books.remove(book)
        print("Book borrowed")
    else:
        print("Not available")

# New function: remove book from library
def remove_book(book):
    if book in books:
        books.remove(book)
        print("Book removed from library")
    else:
        print("Book not found")

# Running the program
show_books()
borrow_book("Math")
show_books()

remove_book("Science")   # testing remove function
show_books()