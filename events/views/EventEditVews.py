from rest_framework.generics import RetrieveUpdateDestroyAPIView
from events.models import Event
from events.serializers import EventSerializer

class EventEditView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer