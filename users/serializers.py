from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from loans.serializers import LoansBooksSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
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
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    is_blocked = serializers.BooleanField(default=False, read_only=True)
  
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
        model = User
        fields = ["loans_books"]

    def get_loans_books(self, obj):
        if obj.loans_books.exists():
            return LoansBooksSerializer(obj.loans_books.all(), many=True).data
        else:
            return []


class IsUserBlockedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["is_blocked"]
