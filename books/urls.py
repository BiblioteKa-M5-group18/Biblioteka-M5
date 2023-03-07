from django.urls import path
from books.views import BooksListView, BookCreateView, BookListByIdView

urlpatterns = [
    path("book/list/", BooksListView.as_view()),
    path("book/", BookCreateView.as_view()),
    path("book/<int:book_id>/", BookListByIdView.as_view())
]