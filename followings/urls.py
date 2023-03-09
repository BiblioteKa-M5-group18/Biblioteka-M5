from django.urls import path
from .views import FollowingCreate, FollowingUpdate


urlpatterns = [
    path("books/<int:book_id>/following/", FollowingCreate.as_view()),
    path("books/<int:pk>/following/update/", FollowingUpdate.as_view()),
]