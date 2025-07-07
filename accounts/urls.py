from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.sign_in_view.as_view(), name='login'),
    path('logout/', views.sign_out_view.as_view(), name='logout'),
    path('register/', views.sign_up_view.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
]