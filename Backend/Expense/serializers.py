from rest_framework import serializers, validators
from .models import Expense
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password
class ExpenseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    amount = serializers.CharField()
    date = serializers.DateField()
    note = serializers.CharField()

    class Meta:
        model = Expense
        fields = "__all__"

    def create(self, validated_data):
        return Expense.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.date = validated_data.get("date", instance.date)
        instance.note = validated_data.get("note", instance.note)
        instance.save()
        return instance

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ("id", "username", "name", "password1", "password2", "email")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password1"],
        )
        return user

    def validate(self, attrs):
        if attrs.get("password1") != attrs.get("password2"):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        try:
            user = CustomUser.objects.get(username=attrs.get("username"))
            if user:
                raise serializers.ValidationError({"username": "A user with this username exists"})
        except CustomUser.DoesNotExist:
            pass
        try:
            user = CustomUser.objects.get(email=attrs.get("email"))
            if user:
                raise serializers.ValidationError({"email": "A user with this email exists"})
        except CustomUser.DoesNotExist:
            return attrs