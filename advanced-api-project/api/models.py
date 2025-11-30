from django.db import models

class Author(models.Model):
    # The Author model represents an author with a name.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    # The Book model represents a book written by an author,
    # with title, publication year, and a foreign key to Author.
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
