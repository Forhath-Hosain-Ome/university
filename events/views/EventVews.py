from core.views import Api_Crud
from events.models import Event
from events.serializers import EventSerializer

class EventView(Api_Crud):
    queryset = Event.objects.all()
    serializer_class = EventSerializer