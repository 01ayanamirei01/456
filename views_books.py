from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    template_name = 'books/detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'isbn', 'publication_year', 'genres', 'co_authors', 'summary']
    template_name = 'books/form.html'
    success_url = reverse_lazy('books:list')

class BookUpdateView(UpdateView):
    model = Book
    pk_url_kwarg = 'book_id'
    fields = ['title', 'author', 'isbn', 'publication_year', 'genres', 'co_authors', 'summary']
    template_name = 'books/form.html'
    success_url = reverse_lazy('books:list')

class BookDeleteView(DeleteView):
    model = Book
    pk_url_kwarg = 'book_id'
    template_name = 'books/confirm_delete.html'
    success_url = reverse_lazy('books:list')
