from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import SignInSerializer

class SignInView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            login(request, serializer.validated_data["user"])
            return Response({"message": "Login successful"}, status=200)
        return Response(serializer.errors, status=401)


# def SignInView(request):
#     pass