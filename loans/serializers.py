from rest_framework import serializers
from .models import Loan


class LoansBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"