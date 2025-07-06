from django.urls import path
from events.views import *

app_name = 'event'  # Namespace for URL reversing

urlpatterns = [
    path('e',EventView.as_view()),
    path('e/<int:pk>',EventView.as_view())
]