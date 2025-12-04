"""
Interactive CLI for Library Inventory Manager.
"""

from pathlib import Path
from library_manager.inventory import LibraryInventory
from library_manager.book import Book


def menu():
    print("\n------ Library Inventory Manager ------")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    return input("Choose an option: ").strip()


def main():
    inventory = LibraryInventory(Path("catalog.json"))

    while True:
        choice = menu()

        # ADD BOOK
        if choice == "1":
            try:
                title = input("Book title: ").strip()
                author = input("Author: ").strip()
                isbn = input("ISBN: ").strip()

                if not title or not author or not isbn:
                    print("All fields are required.")
                    continue

                book = Book(title, author, isbn)
                inventory.add_book(book)
                print("\nBook added successfully!")
            except Exception as e:
                print("Error:", e)

        # ISSUE BOOK
        elif choice == "2":
            isbn = input("Enter ISBN to issue: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save()
                print("Book issued.")
            else:
                print("Book not available or invalid ISBN.")

        # RETURN BOOK
        elif choice == "3":
            isbn = input("Enter ISBN to return: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save()
                print("Book returned.")
            else:
                print("Book is not issued or invalid ISBN.")

        # VIEW ALL
        elif choice == "4":
            all_books = inventory.display_all()
            print("\n".join(all_books) if all_books else "No books in catalog.")

        # SEARCH
        elif choice == "5":
            title = input("Enter title keyword: ").strip()
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        # EXIT
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
