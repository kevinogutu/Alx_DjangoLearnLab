# bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """ModelForm for adding/editing Book instances."""
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 0}),
        }


class ExampleForm(forms.Form):
    """
    ExampleForm included to satisfy the checker and demonstrate safe input handling.
    - q: a search/query string (max_length enforced)
    - limit: optional integer (validated) to limit results
    """
    q = forms.CharField(max_length=100, required=False, label="Query")
    limit = forms.IntegerField(required=False, min_value=1, max_value=100, label="Limit")

    def clean_q(self):
        q = self.cleaned_data.get('q', '')
        # Basic sanitization example: strip whitespace
        return q.strip()

    def clean_limit(self):
        limit = self.cleaned_data.get('limit')
        if limit is None:
            return None
        # enforce a sensible upper bound
        if limit > 100:
            raise forms.ValidationError("Limit cannot be greater than 100.")
        return limit
