from django.urls import path, include
from courses.views import CourseEdit, EnrollmentEdit
from core.urls import router

router.register(r'x',CourseEdit, basename='x')
router.register(r'z',EnrollmentEdit, basename='z')

app_name = 'courses'

urlpatterns = [
    path('', include(router.urls))
    # path('x/', CourseEdit.as_view(), name='Course_List'),
    # path('x/<int:pk>/', CourseEdit.as_view() ,name='Course_Edit'),
    # path('z/', EnrollmentEdit.as_view(), name='Enrollment_List'),
    # path('z/<int:pk>/', EnrollmentEdit.as_view(), name='Enrollment_List'),
]