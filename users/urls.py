from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/login/", views.TokenObtainPairView.as_view()),
]
