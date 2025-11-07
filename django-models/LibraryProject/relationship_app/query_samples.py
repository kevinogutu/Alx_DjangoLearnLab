# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)
books_by_orwell = Book.objects.filter(author=author)
print("Books by", author.name, books_by_orwell)

# 2. List all books in a library
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)
all_books_in_library = library.books.all()
print("Books in", library.name, all_books_in_library)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.create(name="Alice", library=library)
the_librarian = Librarian.objects.get(library=library)
print("Librarian for", library.name, "is", the_librarian.name)
