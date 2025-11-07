# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.views.generic.detail import DetailView
from .models import Book # ensure Library is imported here
from .models import Library
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', { 'books': books })

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# --- Register View ---
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = RegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})


# --- Login View ---
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# --- Logout View ---
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
