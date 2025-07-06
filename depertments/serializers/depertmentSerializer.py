from core.serializers import rf_ModelSerializer
from depertments.models import depertment

class DepertmentSerializer(rf_ModelSerializer):
    class Meta:
        model = depertment
        fields = '__all__'