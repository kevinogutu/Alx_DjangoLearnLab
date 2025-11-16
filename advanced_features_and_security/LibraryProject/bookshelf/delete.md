### **delete.md**  
```markdown
# delete.md

```python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell")
>>> book.delete()
>>> Book.objects.all()
<QuerySet []>