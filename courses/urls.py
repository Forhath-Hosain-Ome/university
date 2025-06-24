from django.urls import path
from courses.views import Course_crud, Course_list

app_name = 'courses'

urlpatterns = [
    path('', Course_list, name='course_list'),
    path('<int:pk>/', Course_crud, name='course_detail'),
]