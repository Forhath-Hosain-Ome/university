from django.urls import path
from . import views

app_name = 'home'  # Namespace for URL reversing

urlpatterns = [
    path('', views.home, name='home'),
]
