from django.urls import path
from . import views

app_name = 'home'  # Namespace for URL reversing

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('privacy_policy/', views.Privacy_PolicyView, name='privacy_policy'),
]