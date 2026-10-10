def push_book(BooksStack, new_book):
    BooksStack.append(new_book)


def pop_book(BooksStack):
    if BooksStack:
        return BooksStack.pop()
    else:
        print("Underflow")
        return None

def peep(BooksStack):
    if BooksStack:
        return BooksStack[-1]
    else:
        print("None")
        return None


def count_books(BooksStack):
    return len(BooksStack)

def display_books(BooksStack):
    if BooksStack:
        print("Books in Stack:")
        for book in BooksStack:
            print(book)
    else:
        print("The stack is empty.")

def main():
    BooksStack = []

    while True:
        print("\n--- BooksStack Operations ---")
        print("1. Push a book")
        print("2. Pop a book")
        print("3. Peep (view top book)")
        print("4. Count books")
        print("5. Display all books")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            publication_year = int(input("Enter publication year: "))
            new_book = {"book_title": book_title, "author_name": author_name, "publication_year": publication_year}
            push_book(BooksStack, new_book)
            print(f"Book '{book_title}' added to the stack.")
        elif choice == 2:
            removed_book = pop_book(BooksStack)
            if removed_book:
                print(f"Removed book: {removed_book}")
        elif choice == 3:
            top_book = peep(BooksStack)
            if top_book:
                print(f"Top book: {top_book}")
        elif choice == 4:
            print(f"Number of books in stack: {count_books(BooksStack)}")
        elif choice == 5:
            display_books(BooksStack)
        elif choice == 6:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
