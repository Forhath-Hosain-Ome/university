from core.serializers import rf_ModelSerializer
from events.models import Event


class EventSerializer(rf_ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'