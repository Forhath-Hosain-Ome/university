from django.urls import path, include
from .views import AdmissonList
from core.urls import router

router.register(r'admit', AdmissonList, basename='admit')

app_name = 'admissons'  # Namespace for URL reversing

urlpatterns = [
    path('', include(router.urls))
]