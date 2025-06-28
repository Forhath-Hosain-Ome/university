from rest_framework import serializers
from depertments.models import depertment

class DepertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = depertment
        fields = '__all__'