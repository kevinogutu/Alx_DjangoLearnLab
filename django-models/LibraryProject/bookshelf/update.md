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