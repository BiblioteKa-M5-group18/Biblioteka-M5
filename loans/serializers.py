from rest_framework import serializers
from .models import Loan


class LoansBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["id", 'date_collected', 'date_limit_return', 'date_returned', 'user', 'copy']
        read_only_fields = ["id", 'date_collected', 'date_limit_return', 'date_returned' ]