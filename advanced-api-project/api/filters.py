import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    """
    Custom filterset for the Book model.
    """
    
    # Allows partial, case-insensitive matching for title
    title = django_filters.CharFilter(lookup_expr='icontains')
    
    # Allows partial, case-insensitive matching for author
    author = django_filters.CharFilter(lookup_expr='icontains')

    # Creates a 'publication_year' filter that queries the 'year' 
    # part of the 'published_date' field.
    publication_year = django_filters.NumberFilter(
        field_name='published_date', 
        lookup_expr='year'
    )
    
    # Bonus: Add an exact match filter for ISBN
    isbn = django_filters.CharFilter(field_name='isbn', lookup_expr='exact')

    class Meta:
        model = Book
        # We define fields here, but the custom definitions above
        # will be used instead of the defaults.
        fields = ['title', 'author', 'publication_year', 'isbn']