from core.views import Api_List, Api_Edit
from events.models import Event
from events.serializers import EventSerializer

class EventView(Api_List, Api_Edit):
    queryset = Event.objects.all()
    serializer_class = EventSerializer