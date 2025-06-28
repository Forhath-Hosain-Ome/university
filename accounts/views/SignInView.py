from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import SignInSerializer


class SignInView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid() and not None:
            user = serializer.validated_data.get('User')
            if user is not None:
                 login(request, user)
                 return Response({"message": "Login successful"}, status=200)
            return Response({"error": "User not found in validated data"}, status=400)
        return Response(serializer.errors, status=401)