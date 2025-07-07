from django.contrib.auth.models import User
from core.serializers import rf_serializers, rf_ModelSerializer


class SignUpSerializer(rf_ModelSerializer):
    password = rf_serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

