from django.urls import path
from courses.views import *

app_name = 'courses'

urlpatterns = [
    path('x', CourseList.as_view()),
    path('x/<int:pk>', CourseEdit.as_view()),
    path('z', EnrollmentList.as_view()),
    path('z/<int:pk>', EnrollmentEdit.as_view()),
]