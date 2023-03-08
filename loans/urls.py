from django.urls import path
from .views import LoanCreateView, LoanDeleteView

urlpatterns = [
    path("/copies/<int:isbn>/loans/", LoanCreateView.as_view()),
    path("/copies/<int:isbn>/loans/", LoanDeleteView.as_view()),
    
]