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