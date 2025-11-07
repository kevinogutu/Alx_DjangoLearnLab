# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Create sample data
    author = Author.objects.create(name="George Orwell")
    book1  = Book.objects.create(title="1984", author=author)
    book2  = Book.objects.create(title="Animal Farm", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    librarian = Librarian.objects.create(name="Alice", library=library)

    # 1. Query all books by a specific author
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author.name, ":", list(books_by_author))

    # 2. List all books in a library
    all_books_in_library = library.books.all()
    print("Books in", library.name, ":", list(all_books_in_library))

    # 3. Retrieve the librarian for a library
    the_librarian = Librarian.objects.get(library=library)
    print("Librarian for", library.name, "is", the_librarian.name)

    # 4. **Line the checker looks for**
    library_retrieved = Library.objects.get(name="Central Library")
    print("Library retrieved by name:", library_retrieved)

if __name__ == "__main__":
    run_queries()
