from django.urls import path
from .views import BookCreateView

urlpatterns = [
    path("book/", BookCreateView.as_view())
]