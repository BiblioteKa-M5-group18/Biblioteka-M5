from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "name", "is_employee", "is_blocked", "is_superuser"]
        read_only_fields = ["id", "is_blocked", "is_superuser"]

    def validate(self, data):
        errors = {}
        email = data.get("email", None)
        username = data.get("username", None)

        if not email:
            errors.update({"email": "This field is required."})
        elif User.objects.filter(email=email).exists():
            errors.update({"email": "email already registered."})

        if not username:
            errors.update({"username": "This field is required."})
        elif User.objects.filter(username=username).exists():
            errors.update({"username": "username already taken."})

        password = data.get("password", None)
        if password:
            try:
                validate_password(password, user=User)
            except serializers.ValidationError as error:
                errors.update({"password": error.detail})
        
        if errors:
            raise serializers.ValidationError(errors)
        
        return data
    
    def create(self, validated_data):
        is_employee = validated_data.pop("is_employee", False)
        user = User.objects.create_user(**validated_data)
        user.username = validated_data.get("username", None)
        user.is_employee = is_employee

        if is_employee:
            user.is_superuser = True
        user.save()
        return user
