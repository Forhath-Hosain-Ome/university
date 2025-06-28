from rest_framework import generics
from courses.models import Course
from courses.serializers import CourseSerializers

class CourseEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers