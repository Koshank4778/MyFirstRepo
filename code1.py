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

show_books()
borrow_book("Math")
show_books()