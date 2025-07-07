from core.serializers import rf_serializers
from django.contrib.auth import authenticate

class SignInSerializer(rf_serializers.Serializer):
    username = rf_serializers.CharField()
    password = rf_serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data["username"], password=data["password"]
        )
        if not user:
            raise rf_serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data
