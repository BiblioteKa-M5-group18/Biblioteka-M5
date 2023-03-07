from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Copy
from .serializers import CopyListSerializer


class CopyList(ListAPIView, PageNumberPagination):
    serializer_class = CopyListSerializer

    def get_queryset(self):
        return Copy.objects.all()