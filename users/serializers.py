from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "address",
        )

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            phone=validated_data['phone'],
            address=validated_data['address'],
        )
        return user


class CurrentUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "address",
        )

    def validate_password(self, value):
        return make_password(value)
