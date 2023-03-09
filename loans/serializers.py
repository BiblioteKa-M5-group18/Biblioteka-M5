from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy

class UserLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "name"]

class CopyLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "title", "author", "pages", "publishing_company", "isbn", "is_loaned"]

class LoansBooksSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Loan.objects.create(**validated_data)
    
    user = UserLoanSerializer(read_only=True)
    copy = CopyLoanSerializer(read_only=True)
    class Meta:
        model = Loan
        fields = ["id", 'date_collected', 'date_limit_return', 'date_returned', 'user', 'copy']
        read_only_fields = ["id", 'date_collected', 'date_limit_return', 'date_returned', "user", "copy"]