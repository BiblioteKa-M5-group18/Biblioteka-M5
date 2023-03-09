from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from loans.models import Loan
from .models import User
from loans.serializers import LoansBooksSerializer

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="username already taken."
            )
        ]
    )
    email = serializers.EmailField(
        max_length=150,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="email already registered."
            )
        ]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "name", "is_employee", "is_blocked", "is_superuser"]
        read_only_fields = ["id", "is_blocked", "is_superuser"]
        extra_kwargs = {
            "is_employee": {"default": False}
        }
  
    def create(self, validated_data):
        if validated_data["is_employee"]:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
      
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class UserLoansSerializer(serializers.ModelSerializer):
    loans_books = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ["loans_books"]
        read_only_fields = ["loans_books"]

    def get_loans_books(self, obj):
        user = self.context["request"].user
        loans = Loan.objects.get(user=user)
        if loans:
            # RETORNAR INFOS DE LOAN
            return loans
        else:
            return []


class IsUserBlockedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["is_blocked"]
        read_only_fields = ["is_blocked"]