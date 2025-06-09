from django.urls import path
from . import views

app_name = 'accounts'  # Namespace for URL reversing

urlpatterns = [
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]