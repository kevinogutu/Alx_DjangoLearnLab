# create.md

```python
>>> from bookshelf.models import Book
>>> book = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

### **retrieve.md**  
```markdown
# retrieve.md

```python
>>> from bookshelf.models import Book
>>> books = Book.objects.all()
>>> books
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
>>> books[0].title, books[0].author, books[0].publication_year
('1984', 'George Orwell', 1949)

### **update.md**  
```markdown
# update.md

```python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984", author="George Orwell")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.get(pk=book.pk)
<Book: Nineteen Eighty-Four by George Orwell (1949)>

### **delete.md**  
```markdown
# delete.md

```python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell")
>>> book.delete()
>>> Book.objects.all()
<QuerySet []>
