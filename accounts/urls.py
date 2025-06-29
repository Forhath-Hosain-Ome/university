from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.SignOutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
]