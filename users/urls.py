from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserCreate

urlpatterns = [
    path("users/", UserCreate.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
]
