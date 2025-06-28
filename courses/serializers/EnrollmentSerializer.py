from courses.models import CourseEnrollment
from rest_framework import serializers

class EnrollmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'