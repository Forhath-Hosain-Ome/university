from rest_framework import serializers
from depertments.models import depertment

class DepertmentSerializer(serializers.ModelSerializers):
    class Meta:
        model = depertment
        fields = '__all__'