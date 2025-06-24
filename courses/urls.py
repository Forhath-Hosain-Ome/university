from django.urls import path
from .views import course_crud, course_list

app_name = 'courses'

urlpatterns = [
    path('', course_list, name='course_list'),
    # path('<int:pk>/', course_crud, name='course_detail'),
]