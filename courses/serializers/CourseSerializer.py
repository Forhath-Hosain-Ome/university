from rest_framework import serializers
from courses.models import Course

class CourseSerializers(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'
    