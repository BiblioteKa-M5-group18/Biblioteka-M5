from rest_framework.generics import CreateAPIView
from .models import Book
from copies.models import Copy
from .serializers import BookSerializer
from copies.serializers import CopySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class BookCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = CopySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        author = serializer.validated_data.get('author')
        pages = serializer.validated_data.get('pages')
        publishing_company = serializer.validated_data.get('publishing_company')
        isbn = serializer.validated_data.get('isbn')

        if not isbn:
            return Response({'isbn': 'This field is required.'}, status=400)

        try:
            book = Book.objects.get(title=title)
        except Book.DoesNotExist:
            book = Book.objects.create(
                title=title,
                author=author,
                pages=pages,
                publishing_company=publishing_company
            )

        try:
            copy = Copy.objects.get(isbn=isbn)
            return Response({'isbn': 'A copy with this ISBN already exists.'}, status=400)
        except Copy.DoesNotExist:
            copy = Copy.objects.create(
                title=title,
                author=author,
                pages=pages,
                publishing_company=publishing_company,
                isbn=isbn,
                book=book
            )

        serializer = CopySerializer(copy)

        return Response(serializer.data, status=201)

    