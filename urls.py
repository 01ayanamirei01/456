from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views_books import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
)
from .api import AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('books/new/', BookCreateView.as_view(), name='new'),
    path('books/<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path('books/<int:book_id>/edit/', BookUpdateView.as_view(), name='edit'),
    path('books/<int:book_id>/delete/', BookDeleteView.as_view(), name='delete'),

    path('', include(router.urls)),
]
