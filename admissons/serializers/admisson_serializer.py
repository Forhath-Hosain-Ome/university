from core.serializers import rf_ModelSerializer
from admissons.models import AdmissonModel

class AdmissonSerializer(rf_ModelSerializer):
    class Meta:
        model = AdmissonModel
        fields = '__all__'