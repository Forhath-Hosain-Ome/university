from courses.models import CourseEnrollment
from rest_framework import serializers

class EnrollmentSerializers(serializers.Serializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'