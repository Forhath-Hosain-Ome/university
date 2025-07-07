from django.urls import path, include
from events.views import EventView
from core.urls import router

router.register(r'event', EventView, basename='event')




app_name = 'event'

urlpatterns = [
    path('', include(router.urls)),
]