def main():
    class Book:

        def __init__(self, title, author, checked_out):
            self.title = title
            self.author = author
            self.checked_out = checked_out

    book1 = Book("To Kill a Mockingbird", "Harper Lee", False)
    book2 = Book("1984", "George Orwell", False)
    book3 = Book("Slaughterhouse 5", "Kurt Vonnegut", False)

    # Create a list of book objects
    shelf = [book1, book2, book3]

    # Try to check out book2 on the shelf and print if it has been checked out
    if shelf[1].checked_out == False:
        shelf[1].checked_out = True
        print(shelf[1].title + " has been checked out")

    # Total the number of available books
    total = 0
    for book in shelf:
        if book.checked_out == False:
            total += 1

    print("There are " + str(total) + " available books")


if __name__ == "__main__":
    main()

