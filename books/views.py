from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView
from books.models import Book
from books.serializers import BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters import rest_framework as filters

class BooksListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("title", "author", "publishing_company")


class BookCreateView(CreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAccountOwner]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListByIdView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request:Request, book_id) -> Response:
        book = get_object_or_404(Book, pk = book_id)

        serializer = BookSerializer(book)

        return Response(serializer.data, status.HTTP_200_OK)
    