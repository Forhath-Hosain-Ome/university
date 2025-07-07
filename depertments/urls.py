from django.urls import path, include
from .views import DepertmentList
from core.urls import router

router.register(r'depertment', DepertmentList, basename='depertment')

app_name = 'depertments'  # Namespace for URL reversing

urlpatterns = [
    path('',include(router.urls))
]