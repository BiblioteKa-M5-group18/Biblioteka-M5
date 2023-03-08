from .models import Loan
from copies.models import Copy
from .serializers import LoansBooksSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

class LoanCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LoansBooksSerializer

    def perform_create(self, serializer):
        copy = get_object_or_404(Copy, isbn=self.kwargs.get("isbn"))
        # CHECAR SE A COPIA JÁ ESTÁ EMPRESTADA
        # if copy.is_loaned == True:
        #     return Response({'isbn': 'A copy with this ISBN already exists.'}, status=400) 
        copy.is_loaned = True
        copy.save()
        return serializer.save(user=self.request.user, copy=copy)


# class LoanReturnView(DestroyAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = Loan.objects.all()
#     serializer_class = LoansBooksSerializer
#     lookup_url_kwarg = "isbn"

    # def perform_destroy(self, instance):
    #     ipdb.set_trace()
        # copy = get_object_or_404(Copy, isbn=self.kwargs.get("isbn"))
        # loan = get_object_or_404(Loan, user=self.request.user, copy=copy)

        # loan.date_returned = timezone.now()
        # loan.copy.is_loaned = False
        
        # return instance.save()

# class LoanReturnView(APIView):
#     def delete(self, request, isbn):
#         copy = get_object_or_404(Copy, isbn=isbn)
#         loan = get_object_or_404(Loan, user=self.request.user, copy=copy)

#         loan.date_returned = timezone.now()
#         loan.copy.is_loaned = False

#         return Response(loan, status=200)