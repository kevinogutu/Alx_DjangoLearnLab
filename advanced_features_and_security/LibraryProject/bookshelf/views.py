# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import BookForm  # simple ModelForm for Book (example below)
from django.db.models import Q
from django import forms
from django.http import HttpResponse
from .forms import ExampleForm   


def book_list(request):
    # listing books - require view permission for more restricted sites (optional)
    # If you want to restrict list view, uncomment decorator below and remove unrestricted version.
    # @permission_required('bookshelf.can_view', raise_exception=True)
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Add'})


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)

def search_books(request):
    form = SearchForm(request.GET)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data['q']
        # safe: ORM parameterizes under the hood
        books = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
    return render(request, "bookshelf/search_results.html", {"form": form, "books": books})
# bookshelf/views.py



def example_view(request):
    """
    Demonstrates safe handling of user input using ExampleForm.
    This view prevents XSS and SQL injection by relying on Django forms + ORM.
    """
    form = ExampleForm(request.GET or None)

    results = []
    if form.is_valid():
        q = form.cleaned_data.get('q')
        limit = form.cleaned_data.get('limit')

        # Safe filtering using Django ORM (no SQL injection)
        if q:
            results = Book.objects.filter(title__icontains=q)

        if limit:
            results = results[:limit]

    return render(request, "bookshelf/example_view.html", {
        "form": form,
        "results": results
    })
