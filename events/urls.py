from django.urls import path, include
from events.views import EventView
from core.urls import router

router.register(r'event', EventView, basename='event')




app_name = 'event'

urlpatterns = [
    # path('e',EventView.as_view()),
    # path('e/<int:pk>',EventView.as_view()),
    path('', include(router.urls))
]