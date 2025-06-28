from rest_framework.generics import RetrieveUpdateDestroyAPIView as crude
from courses.models import CourseEnrollment
from courses.serializers import CourseSerializers



class EnrollmentEdit(crude):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseSerializers