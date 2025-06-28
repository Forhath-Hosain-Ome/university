from rest_framework.generics import ListCreateAPIView
from events.models import Event
from events.serializers import EventSerializer

class EventView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer