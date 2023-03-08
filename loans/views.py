from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import LoansBooksSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# class LoanCreateView(APIView):
#     def post(self, request):
#         serializer

# LoanDeleteView