from rest_framework.generics import ListCreateAPIView as create
from courses.models import CourseEnrollment
from courses.serializers import CourseSerializers

class EnrollmentList(create):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseSerializers