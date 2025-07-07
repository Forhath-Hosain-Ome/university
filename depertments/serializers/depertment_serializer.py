from core.serializers import rf_ModelSerializer
from depertments.models import depertment_model

class DepertmentSerializer(rf_ModelSerializer):
    class Meta:
        model = depertment_model
        fields = '__all__'