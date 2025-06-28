from rest_framework import generics
from depertments.models import Depertment
from depertments.serializers import DepertmentSerializer

class DepertmentList(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Depertment.objects.all()
    serializer_class = DepertmentSerializer

# class DepertmentEdit(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Depertment.objects.all()
#     serializer_class = DepertmentSerializer