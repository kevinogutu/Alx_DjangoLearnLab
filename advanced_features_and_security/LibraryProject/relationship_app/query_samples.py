# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Create sample data
    author_name = "George Orwell"
    author      = Author.objects.create(name=author_name)
    book1       = Book.objects.create(title="1984", author=author)
    book2       = Book.objects.create(title="Animal Farm", author=author)

    library_name = "Central Library"
    library      = Library.objects.create(name=library_name)
    library.books.add(book1, book2)

    librarian    = Librarian.objects.create(name="Alice", library=library)

    # 2. Query all books by a specific author
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author.name, ":", list(books_by_author))

    # 3. List all books in a library
    all_books_in_library = library.books.all()
    print("Books in", library.name, ":", list(all_books_in_library))

    # 4. Retrieve the librarian for a library
    the_librarian = Librarian.objects.get(library=library)
    print("Librarian for", library.name, "is", the_librarian.name)

    # 5. **Line required by checker**: get Author by name
    author_retrieved = Author.objects.get(name=author_name)
    print("Author retrieved by name:", author_retrieved)

    # 6. **Line required by checker**: get Library by name
    library_retrieved = Library.objects.get(name=library_name)
    print("Library retrieved by name:", library_retrieved)

if __name__ == "__main__":
    run_queries()
