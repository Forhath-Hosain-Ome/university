from rest_framework import serializers
from django.contrib.auth import authenticate

class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data["username"], password=data["password"]
        )
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data
